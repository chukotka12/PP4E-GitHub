"""
Обработчик событий на основе метода класса
Не смотря на то, что в tkinter обработчики событий
вызываются без параметров, метод класса неявно передает
в метод quit ссылку на вызывающий объект (self),
 что позволяет использовать значения атрибутов объекта! баг/фича?
"""
import sys
from tkinter import *


class HelloClass:
    def __init__(self):
        widget = Button(None,
                        text='Hello event world',
                        command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class method world')
        sys.exit()


HelloClass()
mainloop()
