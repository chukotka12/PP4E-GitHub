"""
Перемещение с применением тегов и ф-ции time.sleep()
(без помощи метода widget.after или потоков выполнения);
 ф-ция time.sleep не блокирует цикл событий графического интерфейса
 на время паузы, но интерфейс не обновляется до выхода из
обработчика или вызова метода widget.update; текущему вызову обработчика onMove
уделяется исключительное внимание, пока он не вернет управление: если в
процессе перемещения нажать клавишу 'R' или 'O'
"""
from tkinter import *
import canvasDraw, time


class CanvasEventDemo(canvasDraw.CanvasEventDemo):
    def __init__(self, parent=None):
        canvasDraw.CanvasEventDemo.__init__(self, parent)
        self.canvas.create_text(100, 10, text='Press <o> or <r> to move shapes')
        self.canvas.master.bind('<KeyPress-o>', self.onMoveOvals)
        self.canvas.master.bind('<KeyPress-r>', self.onMoveRectangles)
        self.kinds = self.create_oval_tagged, self.create_rectangle_tagged

    def create_oval_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_oval(x1, y1, x2, y2)
        self.canvas.itemconfig(objectId, tab='ovals', fill='blue')
        return objectId

    def create_rectangle_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_rectangle(x1, y1, x2, y2)
        self.canvas.itemconfig(objectId, tag='rectangles', fill='red')
        return objectId

    def onMoveOvals(self, event):
        print('moving ovals')
        self.moveInSquares(tag='ovals')

    def onMoveRectangles(self, event):
        print('moving rectangles')
        self.moveInSquares(tag='rectangles')

    def moveInSquares(self, tag):
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                self.canvas.update()
                time.sleep(0.25)


if __name__ == '__main__':
    CanvasEventDemo()
    mainloop()
