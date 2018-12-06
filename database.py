import sqlite3

class Database:

    def __init__(self):

        self.db = sqlite3.connect('tb-keyvalue-store.db')

        #let's just always be a python dictionary
        def dict_factory(cursor, row):
           d = {}
           for idx, col in enumerate(cursor.description):
               d[col[0]] = row[idx]
           return d
        self.db.row_factory = dict_factory

        self.db.execute('CREATE TABLE IF NOT EXISTS storage (key TEXT PRIMARY KEY, value TEXT)')

        #print all existing keys, for debugging, since it was explicitly permitted
        #for row in self.db.execute('SELECT * from storage').fetchall():
        #    print(row)


    def put_value(self, key, value):
        print 'key', key, 'value', value
        self.db.execute('REPLACE INTO storage (key, value) VALUES (?, ?)', [key,value])
        self.db.commit()

    def read(self, key):
        print 'key', key
        value = ""
        for row in self.db.execute('SELECT value FROM storage WHERE key = ?', [key]).fetchall():
            value = row['value']
            return value #row #exiting on 1st on purpose
        return value

    def delete(self, key):
        print 'deleting ', key
        self.db.execute('delete from storage where key = ?', [key])

    def read_all(self):
        #what kind of struct is this even
        return self.db.execute('SELECT key, value FROM storage').fetchall();
