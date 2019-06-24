#!/usr/local/bin/python
"""
главное меню окна в стиле Tk8.0
строка меню и панель инструментов прикрепляются к окну в первую очередь, fill=X
(прикрепить первым = обрезать последним); добавляет изображения в элементы меню;
смотрите также: add_checkbutton, add_radiobutton
"""
from tkinter import *
from tkinter.messagebox import *


class NewMenuDemo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()
        self.master.title('Toolbars and Menus')  # для менеджера окон
        self.master.iconname('tkpython')  # текст метки при свертывании

    def createWidgets(self):
        self.makeMenuBar()

        # self.makeToolBarTk()
        # вариант добавления image в элементы меню
        # self.makeToolbarPIL()
        # или вариант с предварительной подгонкой размеров изображения
        self.makeToolBar3()

        l = Label(self, text='Menu and Toolbar Demo')
        l.config(relief=SUNKEN, width=40, height=10, bg='white')
        l.pack(expand=YES, fill=BOTH)

    def makeToolBarTk(self):
        """
        на основе tkinter
        """
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Quit', command=self.quit).pack(side=RIGHT)
        Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)

    def makeToolbarPIL(self):
        """
        на основе PIL
        изменяет размеры изображений для кнопок на панели инструментов
        с помощью PIL
        """
        from PIL.ImageTk import PhotoImage, Image  # для jpg и новых миниатюр
        imgdir = r'../PIL/images/'
        size = (50, 50)
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        photos = ('sosnpoln.gif', 'урицк.gif', 'южно-приморский.gif')
        self.toolPhotoObj = []

        for file in photos:
            imgobj = Image.open(imgdir + file)
            imgobj.thumbnail(size, Image.ANTIALIAS)
            img = PhotoImage(imgobj)
            btn = Button(toolbar, image=img, command=self.greeting)
            btn.config(relief=RAISED, bd=2)
            btn.config(width=size[0], height=size[1])
            btn.pack(side=LEFT)
            self.toolPhotoObj.append((img, imgobj))
        Button(toolbar, text='Quit', command=self.quit).pack(side=RIGHT, fill=Y)

    # использовать подготовленные изображения gif и стандартные средства tkinter
    def makeToolBar3(self, size=(30, 30)):
        imgdir = r'../gifs/'
        toolbar = Frame(self, cursor='hand2', relief = SUNKEN, bd = 2)
        toolbar.pack(side=BOTTOM, fill=X)
        photos = 'sosnpoln.gif', 'урицк.gif', 'южно-приморский.gif'
        self.toolPhotoObjs = []
        for file in photos:
            img = PhotoImage(file=imgdir + file)
            btn = Button(toolbar, image=img, command=self.greeting)
            btn.config(bd=5, relief=RIDGE)
            btn.config(width=size[0], height=size[1])
            btn.pack(side=LEFT)
            self.toolPhotoObjs.append(img)  # сохранить ссылку
        Button(toolbar, text='Quit', command = self.quit).pack(side=RIGHT, fill=Y)

    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)  # master - окно верхнего уровня
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

    def imageMenu(self):
        photoFiles = ('sosnpoln.gif', 'урицк.gif', 'южно-приморский.gif')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        for file in photoFiles:
            img = PhotoImage(file='../gifs/' + file)
            pulldown.add_command(image=img, command=self.notdone)
            self.photoObjs.append(img)
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    def greeting(self):
        showinfo('greeting', 'Greetings')

    def notdone(self):
        showerror('Not implemented', 'Not yet available')

    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)


if __name__ == '__main__':
    NewMenuDemo().mainloop()
