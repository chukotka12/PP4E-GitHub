"""
добавляет эквивалентное окно, используя фреймы-ряды и метки фиксированной длины;
использование файомв-колонок не обеспечивает точного взаимного распололжения
виджетов Label и Entry по горизонтали; программный код в обоих случаях имеет
одинаковую длину, хотя применение встроенной функции enemerate позволило бы
сэкономить 2 строки в реализации компоновки по сетке;
"""
from tkinter import *

colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']


def gridbox(parent):
    "компоновка по номерам рядов/колонок в сетке"
    row = 0
    for color in colors:
        lab = Label(parent, text=color, relief=RIDGE, width=25)
        ent = Entry(parent, bg=color, relief=SUNKEN, width=50)
        lab.grid(row=row, column=0)
        ent.grid(row=row, column=1)
        ent.insert(0, 'grid')
        row += 1


def gridbox2(parent):
    "версия табличной компоновки, сокращенная (ловля блох) "
    for (row, color) in enumerate(colors):
        Label(parent, text=color, relief=RIDGE, width=25).grid(row=row, column=0)
        ent = Entry(parent, bg=color, relief=SUNKEN, width=50)
        ent.grid(row=row, column=1)
        ent.insert(0, 'grid')


def packbox(parent):
    "фреймы-ряды и метки фиксированной длины"
    for color in colors:
        row = Frame(parent)
        lab = Label(row, text=color, relief=RIDGE, width=25)
        ent = Entry(row, bg=color, relief=SUNKEN, width=50)
        row.pack(side=TOP)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        ent.insert(0, 'pack')


if __name__ == '__main__':
    root = Tk()
    gridbox(Toplevel())
    packbox(Toplevel())
    Button(root, text='Quit', command=root.quit).pack()
    mainloop()
