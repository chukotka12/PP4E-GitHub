# упаковывает текстовые файлы в единый файл, добавляя строки-разделители
# (простейшая архивация)
import sys, glob

marker = ':' * 20 + 'textpack=>'  # д.б. уникальная строка


def pack(ofile, ifiles):
    output = open(ofile, 'w')
    for name in ifiles:
        print('packing:', name)
        input = open(name, 'r').read()
        if input[-1] != '\n': input += '\n'
        output.write(marker + name + '\n')
        output.write(input)


if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:
        ifiles += glob.glob(patt)  # подстановка по шаблону
    pack(sys.argv[1], ifiles)  # упаковать перечисленные файлы
