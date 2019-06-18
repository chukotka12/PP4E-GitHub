"""
Использование классов в качестве обработчиков событий
Не понятна идея; зачем?
"""
import sys
from tkinter import *

class HelloCallble:
    def __init__(self):
        self.msg='Hello __call__ world'
    def __call__(self):
        print(self.msg)
        sys.exit()
widget=Button(None, text='Hello event world', command=HelloCallble())
widget.pack()
widget.mainloop()