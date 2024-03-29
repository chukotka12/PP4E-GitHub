"""
Действует подобно сценарию System\Filetools\cpall.py, но использует классыобходчики и функцию os.walk; заменяет строку fromDir на toDir перед всеми
именами, возвращаемыми обходчиком; предполагается, что изначально каталог toDir
не существует;
Использование: “python ...\Tools\visitor_cpall.py <fromDir> <toDir> trace?”
"""
import os
from visitor import FileVisitor  # обходчик в каталоге
from System.Filetools.cpall import copyfile


class CpallVisitor(FileVisitor):
    def __init__(self, fromDir, toDir, trace=True):
        self.fromDirLen = len(fromDir) + 1
        self.toDir = toDir
        FileVisitor.__init__(self, trace=trace)

    def visitdir(self, dirpath):
        toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        if self.trace: print('d', dirpath, '=>', toPath)
        os.mkdir(toPath)
        self.dcount += 1

    def visitfile(self, filepath):
        toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
        if self.trace: print('f', filepath, '=>', toPath)
        copyfile(filepath, toPath)
        self.fcount += 1


if __name__ == '__main__':
    import sys, time

    fromDir, toDir = sys.argv[1:3]
    trace = len(sys.argv) > 3
    print('Copying...')
    start = time.process_time()
    walker = CpallVisitor(fromDir, toDir, trace)
    walker.run(startDir=fromDir)
    print('Copied', walker.fcount, 'files', walker.dcount, 'directories',
          end=' ')
    print('in', time.process_time() - start, 'seconds')
