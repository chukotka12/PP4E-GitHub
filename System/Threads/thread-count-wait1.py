"""
использование мьютексов в родительском/главном потоке выполнения
для определения момента завершения дочерних потоков, взамен time.sleep;
блокирует stdout, чтобы избежать конфликтов при выводе;
"""
import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutex = [thread.allocate_lock() for i in range(10)]


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s]=> %s' % (myId, i))
        stdoutmutex.release()
    exitmutex[myId].acquire()  # сигнал главному потоку


for i in range(10):
    thread.start_new_thread(counter, (i, 100))

for mutex in exitmutex:  # !!!
    while not mutex.locked(): pass
print('Main thread exiting.')
