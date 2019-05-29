"""
Сохраняет в файл базу данных, находящуюся в оперативной памяти, используя
собственный формат записи; предполагается, что в данных отсутствуют строки
‘endrec.’, ‘enddb.’ и ‘=>’; предполагается, что база данных является словарем
словарей; внимание: применение функции eval может быть опасным – она
выполняет строки как программный код; с помощью функции eval() можно также
реализовать сохранение словарей-записей целиком; кроме того, вместо вызова
print(key,file=dbfile) можно использовать вызов dbfile.write(key + ‘\n’);
"""
dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


# noinspection PyPep8Naming
def storeDbase(db, dbfilename=dbfilename):
    """сохранение базы данных в файл"""
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
    print(ENDREC, file=dbfile)
    dbfile.close()

def loadDbase(dbfilename = dbfilename):
    """восстанавливает данные, реконструируя базу данных"""
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db={}
    key = input()
    while key !=ENDDB:
        rec={}
        while field !=ENDREC:
            name, value=field.split(RECSEP)
            rec[name]= eval(value)
            field=input()
        db[key]= rec
        key = input()
    return db