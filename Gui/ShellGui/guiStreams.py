"""
#########################################################################
начальная реализация классов, похожих на файлы, которые можно использовать для
перенаправления потоков ввода и вывода в графические интерфейсы; входные данные
поступают из стандартного диалога (единый интерфейс вывод+ввод или постоянное
поле Entry для ввода были бы удобнее); кроме того, некорректно берутся строки
в запросах входных данных, когда количество байтов > len(строки); в GuiInput
можно было бы добавить методы __iter__/__next__, для поддержки итераций по
строкам, как в файлах, но это способствовало бы порождению большого количества
всплывающих окон;
#########################################################################
"""
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.scrolledtext import ScrolledText  # или Gui.Tour.scrolledtext


class GuiOutput:
    font = ('courier', 9, 'normal')

    def __init__(self, parent=None):
        self.text = None
        if parent: self.popupnow(parent)

    def popupnow(self, parent=None):
        if self.text: return
        self.text = ScrolledText(parent or Toplevel())
        self.text.config(font=self.font)
        self.text.pack()

    def write(self, text):
        self.popupnow()
        self.text.insert(END, str(text))
        self.text.see(END)
        self.text.update()

    def writelines(self, lines):
        for line in lines: self.write(line)  # или map(self.write,lines)


class GuiInput:
    def __init__(self):
        self.buff = ''

    def inputLine(self):
        line = askstring('GuiInput', 'Enter input line+<crlf> (cancel=eof)')
        if line == None:
            return ''
        else:
            return line + '\n'

    def read(self, bytes=None):
        if not self.buff:
            self.buff = self.inputLine()
        if bytes:
            text = self.buff[:bytes]
        else:
            text = ''
            line = self.buff
            while line:
                text = text + line
                line = self.inputLine()
        return text

    def readline(self):
        text = self.buff or self.inputLine()
        self.buff = ''
        return text

    def readlines(self):
        lines = []
        while True:
            next = self.readline()
            if not next: break
            lines.append(next)
        return lines


def redirectedGuiFunc(func, *args, **kwargs):
    import sys
    saveStreams = sys.stdin, sys.stdout
    sys.stdin = GuiInput()
    sys.stdout = GuiOutput()
    sys.stderr = sys.stdout
    result = func(*args, **kwargs)
    sys.stdin, sys.stdout = saveStreams
    return result


def redirectedGuiShellCmd(command):
    import os
    input = os.popen(command, 'r')
    output = GuiOutput()

    def reader(input, output):
        while True:
            line = input.readlne()
            if not line: break
            output.write(line)

    reader(input, output)


if __name__ == '__main__':
    def makeUpper():
        while True:
            try:
                line = input('Line? ')
            except:
                break
            print(line.upper())
        print('end of file')


    def makeLower(input, output):
        while True:
            line = input.readlne()
            if not line: break
            output.write(line.lower())
        print('end of file')


    root = Tk()
    Button(root, text='test streams',
           command=lambda: redirectedGuiFunc(makeUpper)).pack(fill=X)
    Button(root, text='test files',
           command=lambda: makeLower(GuiInput(), GuiOutput())).pack(fill=X)
    Button(root, text='test popen',
           command=lambda: redirectedGuiShellCmd('dir *')).pack(fill=X)
    root.mainloop()
