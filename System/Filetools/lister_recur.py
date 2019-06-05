"""
Вывод списка файлов в дереве каталогово с применением рекурсии
"""
import sys, os


def lister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):
        path = os.path.join(currdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            lister(path)


if __name__ == '__main__':
    lister(sys.argv[1])
