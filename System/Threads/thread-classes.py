"""
экземпляры класса Thread, сохраняющие информацию о состоянии и обладающие
методом run() для запуска потоков выполнения; в реализации используется
высокоуровневый и Java-подобный метод join класса Thread модуля threading
(вместо мьютексов и глобальных переменных), чтобы известить главный родительский
поток о завершении дочерних потоков; подробности о модуле threading ищите
в руководстве по стандартной библиотеке;
"""
import threading

class Mytread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId=myId
        self.count=count
        self.mutex=mutex
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex=threading.Lock()
