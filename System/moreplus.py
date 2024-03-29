"""
обеспечивает постраничный вывод в stdout содержимого строки, файла или потока;
если запускается как самостоятельный сценарий, обеспечивает постраничный вывод
содержимого потока stdin или файла, имя которого указывается в виде аргумента
командной строки; когда входные данные поступают через поток stdin, исключается
возможность использовать его для получения ответов пользователя --вместо этого
можно использовать платформозависимые инструменты или графический интерфейс;
"""
import sys


def getreply():
    """
    читает клавишу, нажатую пользователем,
    даже если stdin перенаправлен в файл или канал
    """
    if sys.stdin.isatty():  # если stdin связан с консолью,
        return input('?')  # читать ответ из stdin
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getch()
            return key
        elif sys.platform[:3] == 'linux':
            # import getch ?
            # or ? open('/dev/tty').readlne()[:-1]
            pass
        else:
            assert False, 'platform not supported'


def more(text, numlines=10):
    """
    реализует постраничный вывод содержимого строки в stdout
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines]
        for line in chunk:  print(line)
        if lines and getreply() not in [b'y', b'Y']: break


    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())