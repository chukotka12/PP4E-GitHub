"""
выводит все изображения, найденные в каталоге, открывая новые окна
GIF-файлы поддерживаются стандартными средствами tkinter, но JPEG-файлы будут
пропускаться при отсутствии пакета PIL
"""
import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage

imgdir = 'images'
if len(sys.argv) > 1:
    imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)

main = Tk()
main.title('Viewer')
quit = Button(main, text='Quit all', command=main.quit, font=('courer', 25))
quit.pack()
savephitos = []
for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    win = Toplevel()
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        savephitos.append(imgobj)
    except:
        errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
        Label(win, text=errmsg).pack()
main.mainloop()
