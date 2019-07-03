"""
аналогично, но анимация воспроизводится с применением циклов time.sleep,
выполняемых параллельно в разных потоках, а не с помощью обработчиков
событий, устанавливаемых методом after(), или одного активного цикла time.
sleep; поскольку потоки выполняются параллельно, эта версия также позволяет
перемещать овалы и прямоугольники _одновременно_ и не требует вызывать метод
update для обновления графического интерфейса: фактически вызов метода .update()
в этой версии приводит к краху, хотя некоторые методы холста можно безопасно
использовать в потоках, иначе все это вообще не работало бы;
"""
from tkinter import *
import canvasDraw_tags
import _thread, time

class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):
    def moveEm(self, tag):
        for i in range(5):
            for (diffx, diffy) in [(+20,0),(0,+20), (-20,0), (0,-20)]:
                self.canvas.move(tag, diffx, diffy)
                time.sleep(0.25) # приостановка только этого потока
    def moveInSquares(self, tag):
        _thread.start_new_thread(self.moveEm, (tag,))

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
