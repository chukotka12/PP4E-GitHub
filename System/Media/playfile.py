#!/usr/local/bin/python
"""
##############################################################################
Пытается проигрывать медиафайлы различных типов. Позволяет определять
специализированные программы-проигрыватели вместо использования универсального
приема открытия файла в веб-броузере. В текущем своем виде может не работать
в вашей системе; для открытия аудиофайлов в Unix используются фильтры и команды,
в Windows используется команда start, учитывающая ассоциации с расширениями
имен файлов (то есть для открытия файлов .au, например, она может запустить
проигрыватель аудиофайлов или веб-броузер). Настраивайте и расширяйте сценарий
под свои потребности. Функция playknownfile предполагает, что вы знаете, какой
тип медиафайла пытаетесь открыть, а функция playfile пробует определить тип
файла автоматически, используя модуль mimetypes; обе они пробуют запустить
вебброузер с помощью модуля webbrowser, если тип файла не удается определить.
##############################################################################
"""
import os, sys, mimetypes, webbrowser

helpmsg = """
Sorry: can’t find a media player for ‘%s’ on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""


def trace(*args): print(*args)  # с разделяющими пробелами


##############################################################################
# приемы проигрывания: универсальный и другие: дополните своими приемами
##############################################################################
class MediaTool:
    def __init__(self, runtext=''):
        self.runtext = runtext

    def run(self, mediafile, **options):
        fullpath = os.path.abspath(mediafile)
        self.open(fullpath, **options)


class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')
        player.write(media.read())


class CmdLine(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile
        os.system(cmdline)


class Winstart(MediaTool):
    def open(self, mediafile, wait=False, **other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT ' + mediafile)


class Webbrowser(MediaTool):
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)


##############################################################################
# медиа- и платформозависимые методы: измените или укажите один из имеющихся
##############################################################################
# соответствия платформ и проигрывателей: измените!
audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'),
    'linux2': CmdLine('cat %s > /dev/audio'),
    'sunos4': Filter('/usr/demo/SOUND/play'),
    'win32': Winstart()
    # 'win32': Cmdline(start %s')
}
videotools = {
    'linux32': CmdLine('tkcVideo_c700 %s'),
    'win32': Winstart(),
}
imagetools = {
    'linux2': CmdLine('zimager %s'),
    'win32': Winstart(),
}
texttools = {
    'linux2': CmdLine('vi %s'),
    'win32': CmdLine('notepad %s')
}
apptools = {
    'win32': Winstart()
}
# таблица соответствия между типами файлов и программами-проигрывателями
mimetable = {
    'audio': audiotools,
    'video': videotools,
    'image': imagetools,
    'text': texttools,
    'application': apptools
}


##############################################################################
# интерфейсы высокого уровня
##############################################################################
def trywebbrower(filename, helpmsg=helpmsg, **options):
    """
    пытается открыть файл в веб-броузере
    как последнее средство, если тип файла или платформы неизвестен,
    а также для файлов типа text/html
    """
    trace('trying browser', filename)
    try:
        player = Webbrowser()
        player.run(filename, **options)
    except:
        print(helpmsg % filename)


def playknownfile(filename, playertable={}, **options):
    """
    проигрывает медиафайл известного типа: использует программы-проигрыватели
    для данной платформы или запускает веб-броузер, если для этой платформы не
    определено ничего другого; принимает таблицу соответствий расширений и
    программ-проигрывателей
    """
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)
    else:
        trywebbrower(filename, **options)


def playfile(filename, mimetable=mimetable, **options):
    """
    проигрывает медиафайл любого типа: использует модуль mimetypes для
    определения типа медиафайла и таблицу соответствий между расширениями и
    программами-проигрывателями; запускает веб-броузер для файлов с типом
    text/html, с неизвестным типом и при отсутствии таблицы соответствий
    """
    contenttype, encoding = mimetypes.guess_type(filename)
    if contenttype == None or encoding is not None:
        contenttype = '?/?'
        maintype, subtype = contenttype.split('/', 1)
        if maintype == 'text' and subtype == 'html':
            trywebbrower(filename, **options)
        elif maintype in mimetable:
            playknownfile(filename, mimetable[maintype], **options)
        else:
            trywebbrower(filename, **options)


##############################################################################
# программный код самопроверки
##############################################################################
if __name__ == '__main__':
    # тип медиафайла известен
    playknownfile('sousa.au', audiotools, wait=True)
    playknownfile('ora-pp3e.gif', imagetools, wait=True)
    playknownfile('ora-lp4e.jpg', imagetools)

    # тип медиафайла определяется
    input('Stop players and press Enter')
    playfile('ora-lp4e.jpg')
