"""
отображает изображение с помощью альтернативного объекта из пакета PIL
поддерживает множество форматов изображений; предварительно установите пакет
PIL: поместите его в каталог Lib\site-packages
"""
import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage

imgdir = 'images'
imgfile = 'spb_backyard.jpg'  # поддерживает gif, jpg, png, tiff, и др.
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)  # теперь поддерживает и JPEG!
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())  # показать размер в пикселях при выходе
