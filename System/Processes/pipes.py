"""
Пример организации двунаправленнного канала.
Запускает дочерний процесс/программу, соединяет свои потоки stdin/stdout
с потоками stdout/stdin дочернего процесса -- операции чтения и записи на
стороне родительского процесса отображаются на стандартные потоки ввода-вывода
дочерней программы; напоминает соединение потоков с помощью модуля subprocess;
"""
import os,sys
def spawn(prog, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd= sys.stdout.fileno()

    parentStdin, childStdout= os.pipe() # создание двух каналов IPC
    childStdin, parentStdout = os.pipe() # return inputfd, outoutfd
    pid=os.fork()
    if pid:
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin, stdinFd)   # копия sys.stdin=pipe1[0]
        os.dup2(parentStdout, stdoutFd) # копия sys.stdout=pipe2[1]
    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args= (prog,)+args
        os.execvp(prog, args)
        assert False, 'execvp failed!'

if __name__=='__main__':
    mypid=os.getpid()
    spawn('python','pipes-testchild.py','spam')

    print('Hello 1 from parent', mypid)
    sys.stdout.flush()
    reply=input()
    sys.stderr.write('Parent got: "%s"\n' % reply)

    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])


