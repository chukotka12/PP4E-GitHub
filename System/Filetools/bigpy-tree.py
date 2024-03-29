"""
Отыскивает наибольший файл с исходным программным кодом на языке Python
в дереве каталогов.
Поиск выполняется в каталоге стандартной библиотеки, отображение результатов
выполняется с помощью модуля pprint
"""
import sys, os, pprint
trace = False
if sys.platform.startswith('win'):
    dirname= r'D:\Programs\Python37-32\Lib'
else:
    dirname = r'/usr/lib/Python37-32'
allsizes=[]
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname=os.path.join(thisDir, filename)
            fullsize=os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))
allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])