"""
4 способа запуска одного и того же потока
"""
import threading, _thread


def action(i):
    print(i ** 32)


# подкласс, хранящий собственную информацию о состоянии
class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        print(self.i ** 32)

# 1-ый
Mythread(2).start()

# 2-ой передача простой ф-ции
thread = threading.Thread(target=(lambda: action(2)))
thread.start()

# 3-ий то же самое, но без lambda-ф-ции,
# сохраняющей информацию о состоянии в образуемом ею замыкании
threading.Thread(target=action, args=(2,)).start()

# 4-ый с помощью модуля thread
_thread.start_new_thread(action, (2,))  # полностью процедурный интерфейс
