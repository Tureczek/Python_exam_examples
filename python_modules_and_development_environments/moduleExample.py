

string = 'This is a string from a module'
module_list = [1, 2, 3, 4, 5, 6, 100]



def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(10))
print(fibonacci(11))
print(fibonacci(8))
print(fibonacci(17))
