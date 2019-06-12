"""
От класса Process можно породить подкласс, так же, как от класса threading.Thread;
объект Queue действует подобно queue.Queue, но обеспечивает обмен данными между
процессами, а не между потоками выполнения
"""
import os, time, queue
from multiprocessing import Process, Queue


# общая очередь для процессов
# очередь - это канал + блокировки/семафоры
class Counter(Process):
    label = ' @'

    def __init__(self, start, queue):
        self.state = start
        self.post = queue
        Process.__init__(self)

    def run(self):
        for i in range(3):
            time.sleep(1) # имитация длительного процесса
            self.state += 1
            print(self.label, self.pid, self.state)
            self.post.put([self.pid, self.state])
        print(self.label, self.pid, '-')


if __name__ == '__main__':
    print('start', os.getpid())
    expected = 9

    post = Queue()
    p = Counter(0, post)  # запустить 3 процесса, использующих общую очередь
    q = Counter(100, post)  # потомки являются производителями
    r = Counter(100, post)
    p.start()
    q.start()
    r.start()

    while expected:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data...')
        else:
            print('posted:', data)
            expected -= 1

    p.join()
    q.join()
    r.join()  # дождаться завершения дочерних процессов
    print('finish', os.getpid(), r.exitcode)  # exitcode - код завершения потомка
