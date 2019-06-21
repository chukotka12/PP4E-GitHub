gifdir = '../gifs/'
from tkinter import *
from PIL.ImageTk import PhotoImage

win = Tk()
# img=PhotoImage(file=gifdir+'templates.gif')       # tkinter
img = PhotoImage(file=gifdir + 'n900.jpeg') # PIL
can = Canvas(win)
can.pack(fill=BOTH)

can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
