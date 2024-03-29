"""
Синхронизация доступа к глобальным объектам (stdout):
так как это общий глобальный объект, данные,
которые выводятся из потоков выполнения, могут перемешиваться, если не
синхронизировать операции
"""
import _thread as thread, time
import threading


def counter(myId, count):
    for i in range(count):
        time.sleep(1)

        mutex.acquire()

        print('[%s]=> %s' % (myId, i))

        mutex.release()


mutex = thread.allocate_lock()  # создание объекта блокировки
for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print('Main thread exiting.')
