# значения могут извлекаться из StringVar и после уничтожения виджета
from tkinter import *
from entry3 import makeform, fetch, fields


def show(variables, popup):
    popup.destroy()  # удаление модальной формы
    fetch(variables)


def ask():
    popup = Toplevel()
    vars = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(vars, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
