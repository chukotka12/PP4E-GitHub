"""
Демонстрация дополнительных возможностей тегов и виджета Text
"""
from tkinter import *

root = Tk()


def hello(event): print('Got tag event')


# создать и настроить виджет Text
text = Text()
text.config(font=('courier', 15, 'normal'))
text.config(width=20, height=12)
text.pack(expand=YES, fill=BOTH)
text.insert(END, 'This is\n\n the meaning\n\nof life. \n\n')

# встроить окна и изображения
btn = Button(text, text='Spam', command=lambda: hello(0))
btn.pack()
text.window_create(END, window=btn)
text.insert(END, '\n\n')
img = PhotoImage(file='../gifs/Templates.gif')
text.image_create(END, image=img)

# применить теги к подстрокам
text.tag_add('demo', '1.5', '1.7')
text.tag_add('demo', '3.0', '3.3')
text.tag_add('demo', '5.3', '5.7')
text.tag_config('demo', background='purple')
text.tag_config('demo', foreground='white')
text.tag_bind('demo', '<Double-1>', hello)
root.mainloop()
