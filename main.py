from generators_decorators_context_manager.decorators import before_and_after, timer, time_stamp, cache, count_calls

print("test")
# Showing a simple decorator
def hello_function():
    print('Hello world')


# hello_function = before_and_after(hello_function)

# hello_function()


# Can also be called like this

@before_and_after
def deco_function():
    hello_function()

#deco_function()


# Why are we using functools

#print(deco_function, '\n')
#print(deco_function.__name__, '\n')
#print(help(deco_function), '\n')



########################################################################################################################


@timer
@time_stamp
def waste_some_time(num_times):
    for i in range(num_times):
        sum([i**2 for i in range(100000)])

#waste_some_time(10)
#waste_some_time(1)




########################################################################################################################

# Caching return values

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

#print(fibonacci(10))
#print(fibonacci(11))
#print(fibonacci(8))
#print(fibonacci(17))

