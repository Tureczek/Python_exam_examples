import pymongo

# context managers are used for managing resources

# Consuming file descriptor resources
def cons_resources():
    file_descriptor = []
    for x in range (10000):
        file_descriptor.append(open('test.txt', 'w'))



# try-except-finally -> context managers

class ContextManager(): # Importent to implement the enter() and exit() methods
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')

    def __exit__(self, exc_type, exc_val, exc_tb): # managing exceptions
        print('exit method called')

with ContextManager() as manager:
    print('statement body - in this block the code goes')

########################################################################################################################
# File management with context manager and a statement

class FileManager:
    def __init__(self, filename, mode): # Create object (constructor)
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self): # Opens file and returns ad object to variable f
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Opening a file with FileManager
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed) # Has already been taken care of.



########################################################################################################################
# Managing a database
'''
class MongoDBConnector:
    def __init__(self, hostname, port):
       self.hostname = hostname
       self.port = port
       self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

with MongoDBConnector('localhost', '27017') as mongo:
    collection = mongo.connection.sampleDB.test
    data= collection.find({'_id': 1})
    print(data.get('name'))
'''

