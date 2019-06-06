"""
объект мьютекса, совместно используемый всеми потоками выполнения, передается
функции в виде аргумента; для автоматического приобретения/освобождения
блокировки используется менеджер контекста; чтобы избежать излишней нагрузки
в цикле ожидания, и для имитации выполнения продолжительных операций добавлен
вызов функции sleep
"""
import _thread as thread, time

stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutex = [thread.allocate_lock() for i in range(numthreads)]


def couter(myId, count, mutex):  # мьютекс передается в аргументах
    for i in range(count):
        time.sleep(1 / (myId + 1))
        with mutex:
            print('[%s]=> %s' % (myId, i))
    exitmutex[myId].acquire()  # глобальный список: сигнал главному потоку


for i in range(numthreads):
    thread.start_new_thread(couter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutex): time.sleep(0.25)
print('Main thread exiting.')
