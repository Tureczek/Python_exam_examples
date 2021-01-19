# from pymongo import MongoClient

import sqlite3


# context managers are used for managing resources

# Consuming file descriptor resources
def cons_resources():
    file_descriptor = []
    for x in range(10000):
        file_descriptor.append(open('test.txt', 'w'))


# try-except-finally -> context managers

class ContextManager():  # Importent to implement the enter() and exit() methods
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')

    def __exit__(self, exc_type, exc_val, exc_tb):  # managing exceptions
        print('exit method called')


# with ContextManager() as manager:
#    print('statement body - in this block the code goes')

########################################################################################################################
# File management with context manager and a statement

class FileManager:
    def __init__(self, filename, mode):  # Create object (constructor)
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):  # Opens file and returns as object to variable f
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Opening a file with FileManager
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)  # Has already been taken care of.


########################################################################################################################
# Managing a database

class dbopen(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    with dbopen('./testdb.db') as db:
        db.execute("CREATE TABLE IF NOT EXISTS python_user (id int, name text, age int)")
        db.execute("INSERT INTO python_user VALUES (1, 'Thomas', 31)")
        db.execute("INSERT INTO python_user VALUES (2, 'Bo', 35)")
        db.execute("INSERT INTO python_user VALUES (3, 'Lotte', 21)")
        db.execute("SELECT * FROM python_user")
        result = db.fetchall()
        print(result)

