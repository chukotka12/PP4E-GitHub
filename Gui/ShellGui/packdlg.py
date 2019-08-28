# выводит диалог ввода параметров для сценария packer и запускает его
from glob import glob  # расширение шаблонов имен файлов
from tkinter import *
from packer import pack
from formrows import makeFormRow


def packDialog():
    win = Toplevel()  # окно верхнего уровня с 2 фреймами-рядами+кнопка Ок
    win.title('Enter Pack Parameters')
    var1 = makeFormRow(win, label='Output file')
    var2 = makeFormRow(win, label='Files to pack', extend=True)
    Button(win, text='Ok', command=win.destroy).pack()
    win.grab_set()  # модальный: захват мышь, фокус
    win.focus_set()
    win.wait_window()  # ожидание закрытия
    return var1.get(), var2.get()


def runPackDialog():
    output, patterns = packDialog()
    if output != '"and patterns !="':
        patterns = patterns.split()
        filenames = []
        for sublist in map(glob, patterns):
            filenames += sublist
        print('Packer:', output, filenames)
        pack(ofile=output, ifiles=filenames)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command=runPackDialog).pack(fill=X)
    Button(root, text='bye', command=root.quit).pack(fill=X)
    root.mainloop()
