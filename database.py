import sqlite3

class Database:

    def __init__(self):

        self.db = sqlite3.connect('tb-keyvalue-store.db')

        self.cursor = self.db.cursor()

        self.cursor.execute('CREATE table IF NOT EXISTS storage (key text, value text)')

        #print all existing keys, for debugging, since it was explicitly permitted
        for row in self.cursor.execute('SELECT * from storage'):
            print(row)


    def put_value(key, value):
        print('key: ? value?', [key], [value])

    #def read(key):


    #def read_all():
    #ok


    def delete(key):
        print([key])
        self.cursor.execute('delete from storage where key = ?', [key])
