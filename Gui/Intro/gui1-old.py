# старый стиль (до версии Python 1.3), но действующий!
from tkinter import *
Label(None, {'text':'Hello GUI world!', Pack:{'side':'top'}}).mainloop()
"""
или
options = {'text': 'Hello GUI world!'}
layout = {'side': 'top'}
Label(None, **options).pack(**layout) # ключи должны быть строками
"""