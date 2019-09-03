"""
демонстрирует запуск двух отдельных циклов mainloop; каждый из них возвращает
управление после того как главное окно будет закрыто; ввод пользователя
сохраняется в объекте Python перед тем, как графический интерфейс будет
закрыт; обычно в программах с графическим интерфейсом настройка виджетов
и вызов mainloop выполняется всего один раз, а вся их логика распределена
по обработчикам событий; в этом демонстрационном примере вызовы функции
mainloop производятся для обеспечения модальных взаимодействий с пользователем
из программы командной строки; демонстрирует один из способов добавления
графического интерфейса к существующим сценариям командной строки без
реорганизации программного кода;
"""
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text='Basic demo').pack()
        Button(self, text='open', command=self.openfile).pack(fill=BOTH)
        Button(self, text='save', command=self.savefile).pack(fill=BOTH)
        self.open_name = self.save_name = ''

    def openfile(self):
        self.open_name = askopenfilename()

    def savefile(self):
        self.save_name = asksaveasfilename(inialdir='C:\\')


if __name__ == '__main__':
    print('popup1...')
    mydialog = Demo()  # присоединить фрейм к окну Tk() по умолчанию
    mydialog.mainloop()  # отобразить; вернуться после закрытия окна
    print(mydialog.open_name)  # имена сохраняются в объекте, когда окно уже будет закрыто
    print(mydialog.save_name)

    # ... раздел программы без графич. интерфейса

    # отобразить окно еще раз
    print('popup2 ...')
    mydialog = Demo()  # повтороное создание виджета
    mydialog.mainloop()  # повторное отображение
    print(mydialog.open_name)
    print(mydialog.save_name)

    print('ending...')
