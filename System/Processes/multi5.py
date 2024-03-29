"""
Использует пакет multiprocessing для запуска независимых программ,
с помощью os.fork или других функций
"""
import os
from multiprocessing import Process

def runprogram(arg):
    os.execlp('python', 'python', 'child.py', str(arg))

if __name__=='__main__':
    for i in range(5):
        Process(target=runprogram, args=(i,)).start()
    print('parent exit')