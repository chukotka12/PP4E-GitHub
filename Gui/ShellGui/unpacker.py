# распаковывает архивы, созданные сценарием packer.py
# (простейшие архивы текстовых файлов)
import sys
from packer import marker  # общая строка-разделитель

mlen = len(marker)  # имена файлов идут за строкой-разделителем


def unpack(ifile, prefix='new-'):
    for line in open(ifile):
        if line[:mlen] != marker:
            output.write(line)
        else:
            name = prefix + line[mlen:-1]
            print('creating:', name)
            output = open(name, 'w')


if __name__ == '__main__':
    unpack(sys.argv[1])
