gifdir='../gifs/'
from tkinter import *
win = Tk()
igm=PhotoImage(file=gifdir+'spb_bw1.gif')
Button(win, image=igm).pack()
win.mainloop()