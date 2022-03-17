import sqlite3 as sq
import sqlite3

base = sq.connect('database.db')
cur = base.cursor()

def all_user():
    base.execute('\
    CREATE TABLE IF NOT EXISTS user(\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        user_id VARCHAR (255) NOT NULL,\
        status BBOLEAN NOT NULL DEFAULT (TRUE))')

class all_user_class:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `user_id` = ?', (user_id,)).fetchmany(1)
            return bool(len(result))
    
    async def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO `user` (user_id) VALUES (?)', (user_id,))