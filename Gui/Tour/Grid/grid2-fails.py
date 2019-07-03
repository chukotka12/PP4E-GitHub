"""
Ошибка - методы pack и grid не могут одновременноо использоваться в одном и том эе
родительском контейнере (здесь, корневое окно)
Работать не будет. В виндах - подвешивает процесс в linux:
cannot use geometry manager pack inside . which already has slaves managed by grid
"""
from tkinter import *
from grid2 import gridbox, packbox

root = Tk()

# """
# работоспособный вариант:
# """
# frm = Frame(root)
# frm.pack()
# gridbox(frm)

gridbox(root)

packbox(root)

Button(root, text='Quit', command=root.quit).pack()
mainloop()
