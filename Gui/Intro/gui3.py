"""
Создание собственного обработчика событий
"""
import sys
from tkinter import *


def quit():
    print('Hello, I must be gouing...')
    sys.exit()


widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()
