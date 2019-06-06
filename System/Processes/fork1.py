"""
Ответвляет дочерние процессы, пока не будет нажата клавиша 'q'
Comment: на windows 7 - ошибка: module 'os' has no attribute 'fork'
windows не поддерживает ветвление процессов! Необходимо использовать
Python для Cygwin
"""

import os

def child():
    print('Hello from child', os.getpgid())
    os._exists(0)  # иначе произойдет возврат в родительский цикл

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpgid(), newpid)
        if input()== 'q': break

parent()