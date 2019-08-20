"""
##########################################################################
Расширенный Frame, автоматически создающий меню и панели инструментов в окне.
GuiMakerFrameMenu предназначен для встраивания компонентов (создает меню на
основе фреймов).
GuiMakerWindowMenu предназначен для окон верхнего уровня (создает меню Tk8.0).
Пример древовидной структуры приводится в реализации самотестирования (и
в PyEdit).
##########################################################################
"""
import sys
from tkinter import *  # классы виджетов
from tkinter.messagebox import showinfo


class GuiMaker(Frame):
    menuBar = []  # значения по умолчанию
    toolBar = []  # изменять при создании подклассов
    helpButton = True  # устанавливать в start()

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # растягиваемый фрейм
        self.start()  # в подклассе: установить меню/панель инстр.
        self.makeMenuBar()  # создать полосу меню
        self.makeToolBar()  # создать панель инструментов
        self.makeWidgets()  # добавить середину

    def makeMenuBar(self):
        """
        создает полосу меню вверху (реализация меню Tk8.0 приводится ниже)
        expand=no, fill=x, чтобы ширина оставалась постоянной
        """
        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)

        for (name, key, items) in self.menuBar:
            mbutton = Menubutton(menubar, text=name, underline=key)
            mbutton.pack(side=LEFT)
            pulldown = Menu(mbutton)
            self.addMenuItems(pulldown, items)
            mbutton.config(menu=pulldown)
        if self.helpButton:
            Button(menubar, text='Help',
                   cursor='gumby',
                   relief=FLAT,
                   command=self.help).pack(side=RIGHT)

    def addMenuItems(self, menu, items):
        for item in items:
            if item == 'separator':
                menu.add_separator({})
            elif type(item) == list:
                for num in item:
                    menu.entryconfig(num, state=DISABLED)
            elif type(item[2]) != list:
                menu.add_command(label=item[0],
                                 underline=item[1],
                                 command=item[2])

    def makeToolBar(self):
        """
        создает панель с кнопками внизу, если необходимо
        expand=no, fill=x, чтобы ширина оставалась постоянной
        можно добавить поддержку изображений: смотрите главу 9,
        для чего придется создать минатюры в формате FIF или использовать
        расширение PIL
         """
        if self.toolBar:
            toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            toolbar.pack(side=BOTTOM, fill=X)
            for (name, action, where) in self.toolBar:
                Button(toolbar, text=name, command=action).pack(where)

    def makeWidgets(self):
        """
        ‘средняя’ часть создается последней, поэтому меню/панель инструментов
        всегда остаются вверху/внизу и обрезаются в последнюю очередь;
        переопределите этот метод,
        для pack: прикрепляйте середину к любому краю;
        для grid: компонуйте середину по сетке во фрейме, который
        прикрепляется методом pack
        """
        name = Label(self, width=40, height=10,
                     relief=SUNKEN, bg='white',
                     text=self.__class__.__name__,
                     cursor='crosshair')
        name.pack(expand=YES, fill=BOTH, side=TOP)

    def help(self):
        "Переопределяется в подклассе"
        showinfo('Help', 'Sorry, no help for ' + self.__class__.__name__)

    def start(self):
        "переопределите в подклассе: связать меню/панель инструментов с self"
        pass


##############################################################################
# Специализированная версия для полосы меню главного окна Tk 8.0
##############################################################################
GuiMakerFrameMenu = GuiMaker
