"""
отображает изображение с помощью стандартного объекта PhotoImage из библиотеки tkinter; данная реализация может работать с GIF-файлами, но не может
обрабатывать изображения в формате JPEG; использует файл с изображением, имя
которого указано в командной строке, или файл по умолчанию; используйте Canvas
вместо Label, чтобы обеспечить возможность прокрутки, и т.д.
"""
import os,sys
from tkinter import *

imgdir='images'
imgfile='spb_winter1.png'
if len(sys.argv)>1:
    imgfile = sys.argv[1]
imgpath=os.path.join(imgdir, imgfile)

win=Tk()
win.title(imgfile)
imgobj=PhotoImage(file=imgpath)
Label(win, image= imgobj).pack()
print(imgobj.width(),imgobj.height())
win.mainloop()