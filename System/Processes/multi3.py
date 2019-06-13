"""
Реализует взаимодействие с помощью объектов разделяемой памяти из пакета.
В Windows передаваемые объекты используются совместно, а глобальные объекты
- нет. Последняя проверка здесь отражает типичный случай использования:
распределение заданий между процессами.
"""
import os
from multiprocessing import Process, Value, Array

procs = 3
count = 0


def showdata(label, val, arr):
    """
    вывод значений данных в проессе
    """
    msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
    print(msg % (label, os.getpid(), count, val.value, list(arr)))


def updater(val, arr):
    """
    Обмен данными через разделяему память
    """
    global count
    count += 1
    val.value += 1
    for i in range(3): arr[i] += 1


if __name__ == '__main__':
    scalar = Value('i', 0)
    vector = Array('d', procs)
    # вывод начального значения в родительскомм процессе
    showdata('parent start', scalar, vector)

    # порождение дочернего процесса и передача данных в разделяемую память
    p = Process(target=showdata, args=('child ', scalar, vector))
    p.start();
    p.join()

    # 1. изменение значения в родителе и передача через разделяему память,
    # ожидание завершения каждого потомка
    # все потомки видят изменения, выполенные в родительском процессе и
    # переданные в виде аргументов (но не в глобальной памяти)

    print('\nloop1(updates in parent, parallel children)...')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start(); p.join()

    # 2. то же самоей, но потомки запускаются параллельно
    # все видят результат последней итерации, потому что они хранятся
    # в совместно используемых объектах
    print('\nloop2 (updated in parent, parallel children)...')
    ps=[]
    for i in range(procs):
        count+=1
        scalar.value+=1
        vector[i]+=1
        p=Process(target=showdata, args=(('process %s' % i), scalar, vector))

        p.start()
        ps.append(p)
    for p in ps: p.join()


    # 3. объекты в разделяемой памяти изменяются потомками,
    # ожидание завершения каждого из них
    print('\nloop3 (updates in serial children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
        showdata('parent temp', scalar, vector)

    # 4. то же самое, но потомки запускаются параллельно
    ps = []
    print('\nloop4 (updates in parallel children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps: p.join()

    # глобальная переменная count=6 доступна только родителю
    # выведет последние результаты # scalar=12: +6 в родителе, +6 в 6 потомках
    showdata('parent end', scalar, vector)  # array[i]=8: +2 в родителе, +6 в 6 потомках
