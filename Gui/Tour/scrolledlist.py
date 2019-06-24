"""
простой настраиваемый компонент окна списка с прокруткой
"""
from tkinter import *


class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.runCommand(label)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)  # связать sbar и list
        list.config(yscrollcommand=sbar.set)  # сдвиг одного = сдвиг другого
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0
        for label in options:
            list.insert(pos, label)
            pos += 1
        # list.config(selectmode=SINGLE, setgrid=1) # режимы выбораб изм.размера
        list.bind('<Double-1>', self.handleList)  # установка обработчика событий
        self.listbox = list

    def runCommand(self, selection):  # необходимо переопределить
        print('You selected: ', selection)


if __name__ == '__main__':
    options = (('Lumber jack-%s' % x) for x in range(20))
    ScrolledList(options).mainloop()
