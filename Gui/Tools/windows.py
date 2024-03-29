"""
##############################################################################
Классы, инкапсулирующие интерфейсы верхнего уровня.
Позволяют создавать главные, всплывающие или присоединяемые окна; эти классы
могут наследоваться непосредственно, смешиваться с другими классами или
вызываться непосредственно, без создания подклассов; должны подмешиваться после
(то есть правее) более конкретных прикладных классов: иначе подклассы будут
получать методы (destroy, okayToQuit) из этих, а не из прикладных классов,
и лишатся возможности переопределить их.
##############################################################################
"""
import os, glob
from tkinter import Tk, Toplevel, Frame, YES, BOTH, RIDGE
from tkinter.messagebox import showinfo, askyesno


class _window:
    """
    подмешиваемый класс, используется классами главных и всплывающих окон
    """
    foundicon = None
    iconpatt = '*.ico'
    iconmine = 'py.ico'

    def configBorders(self, app, kind, iconfile):
        if not iconfile:
            iconfile = self.findIcon()
            title = app
            if kind: title += '-' + kind
            self.title(title)
            self.iconname(app)
            if iconfile:
                try:
                    self.iconbitmap(iconfile)
                except:
                    pass
            self.protocol('WM_DELETE_WINDOWS', self.quit)

    def findIcon(self):
        if _window.foundicon:
            return _window.foundicon
        iconfile = None
        iconshere = glob.glob(self.iconpatt)
        if iconshere:
            iconfile = iconshere[0]
        else:
            mymod = __import__(__name__)
            path = __name__.split('.')
            for mod in path[1:]:
                mymod = getattr(mymod, mod)
            mydir = os.path.dirname(mymod.__file__)
            myicon = os.path.join(mydir, self.iconmine)
            if os.path.exists(myicon): iconfile = myicon
        _window.foundicon = iconfile
        return iconfile


class MainWindow(Tk, _window):
    """
    главное окно верхнего уровня
    """

    def __init__(self, app, kind='', iconfile=None):
        Tk.__init__(self)
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if self.okayToQuit():
            if askyesno(self.__app, 'Verify Quit Program?'):
                self.destroy()
        else:
            showinfo(self.__app, 'Quit not allowed')

    def destroy(self):
        Tk.quit(self)

    def okayToQuit(self):
        return True


class PopupWindow(Toplevel, _window):
    """
    вторичное всплывающее окно
    """

    def __init__(self, app, kind='', iconfile=None):
        Toplevel.__init__(self)
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if askyesno(self.__app, 'Verify Quit Window?'):
            self.destroy()

    def destroy(self):
        Toplevel.destroy(self)


class QuietPopupWindow(PopupWindow):
    def quit(self):
        self.destroy()


class ComponentWindow(Frame):
    """
    при присоединении к другим интерфейсам
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.config(relief=RIDGE, border=2)

    def quit(self):
        showinfo('Quit', 'Not supported in attachment mode')
        # destroy из фрейма: просто удалить фрейм
