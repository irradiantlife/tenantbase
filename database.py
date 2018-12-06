import sqlite3

class Database:

    def __init__(self):

        self.db = sqlite3.connect('tb-keyvalue-store.db')

        self.cursor = self.db.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS storage (key TEXT PRIMARY KEY, value TEXT)')

        #print all existing keys, for debugging, since it was explicitly permitted
        for row in self.cursor.execute('SELECT * from storage'):
            print(row)


    def put_value(self, key, value):
        print 'key', key, 'value', value
        self.cursor.execute('REPLACE INTO storage (key, value) VALUES (?, ?)', [key,value])

    def read(self, key):
        print 'key', key
        for row in self.cursor.execute('SELECT value FROM storage WHERE key = ?', [key]):
            print row
            return row #exiting on 1st on purpose

    def delete(self, key):
        print 'deleting ', key
        self.cursor.execute('delete from storage where key = ?', [key])

    def read_all(self):
        #what kind of struct is this even
        return self.cursor.execute('SELECT key, value FROM storage')
