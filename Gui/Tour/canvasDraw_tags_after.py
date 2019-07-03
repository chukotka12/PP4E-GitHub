"""
аналогично, но с применением метода widget.after() вместо циклов time.sleep;
поскольку это планируемые события, появляется возможность перемещать овалы
и прямоугольники _одновременно_ и отпадает необходимость вызывать метод update
для обновления графического интерфейса; движение станет беспорядочным, если еще
раз нажать ‘o’ или ‘r’ в процессе воспроизведения анимации: одновременно начнут
выполняться несколько операций перемещения;
CanvasEventsDemo"""
from tkinter import *
import canvasDraw_tags

class CanvasEventsDemo(canvasDraw_tags.CanvasEventsDemo):


    def moveEm(self, tag, moremoves):
        (diffx,diffy), moremoves=moremoves[0], moremoves[1:]
        self.canvas.move(tag, diffx,diffy)
        if moremoves:
            self.canvas.after(250, self.moveEm, tag, moremoves)


    def moveInSquares(self, tag):
            allmoves= [(+20, 0), (0, +20), (-20, 0), (0, -20)]*5
            self.moveEm(tag, allmoves)


if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
