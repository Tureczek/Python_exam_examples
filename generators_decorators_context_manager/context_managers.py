# context managers are used for managing resources

# Consuming file descriptor resources
def cons_resources():
    file_descriptor = []
    for x in range (10000):
        file_descriptor.append(open('test.txt', 'w'))



# try-except-finally -> context managers

class contextManager(): # Importent to implement the enter() and exit() methods
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')

    def __exit__(self, exc_type, exc_val, exc_tb): # managing exceptions
        print('exit method called')

with contextManager() as manager:
    print('statement body - in this block the code goes')
