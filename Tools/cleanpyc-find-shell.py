"""
отыскивает и удаляет все файлы “*.pyc” с байт-кодом в дереве каталогов, имя
которого передается в виде аргумента командной строки; предполагает наличие
непереносимой Unix-подобной команды find
"""
import os, sys

rundir = sys.argv[1]
if sys.platform[:3] == 'win32':
    findcmd = r'c:\cygwin64\bin\find %s -name "*.pyc" -print' % rundir
else:
    findcmd = 'find %s -name "*.pyc" -print' % rundir

print(findcmd)

count = 0
for fileline in os.popen(findcmd):
    count += 1
    print(fileline, end='')
    os.remove(fileline.rstrip())
print('Removed %d .pyc files' % count)
