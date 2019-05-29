from initdata import db
import pickle

dbfile = open('people-pikle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
