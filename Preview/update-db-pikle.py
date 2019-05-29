import pickle

dbfile = open('people-pikle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *=1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-pikle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()