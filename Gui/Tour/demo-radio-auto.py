# переключатели, простой способ
from tkinter import *

root=Tk()
var = IntVar(0)  # выбор 0-ого переключателя при запуске
for i in range(10):
    rad = Radiobutton(root, text=str(i), value=i, variable=var)
    rad.pack(side=LEFT)
root.mainloop()
print(var.get())
