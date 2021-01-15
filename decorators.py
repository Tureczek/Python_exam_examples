'''
Decorators

Going through:

- What are they.
- How to manipulate .
- When do we use them.
- Why do we use them.

'''
import functools
from datetime import datetime
import time
import logging


# Simple decorator

def before_and_after(func):
    def wrapper():  # decorators wrap a function, modifying its behavior.
        print('This is printed before the function')
        func()
        print('This is printed after the function')

    return wrapper

########################################################################################################################


# Time decorator
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args):
        start_time = time.perf_counter()
        value = func(*args)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f'Finished {func.__name__!r} in {runtime:4f} seconds')
        return value

    return wrapper_timer


########################################################################################################################

# Time stamp

logging.basicConfig(level=logging.INFO, filename="time_stamp.log")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def time_stamp(func):
    @functools.wraps(func)
    def wrapper_time_stamp(*args):
        wrapper_time_stamp.time_call = current_time
        print(f'Call at {wrapper_time_stamp.time_call} of function {func.__name__!r}')
        logging.info(f" Call at {wrapper_time_stamp.time_call} of function {func.__name__!r} with the value {func(*args)!r}")
        return func(*args)
    wrapper_time_stamp.time_call = 0
    return wrapper_time_stamp


########################################################################################################################

# cashing of previous function calls and counting number of times the function is called.

def cache(func):
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f'Call {wrapper_count_calls.num_calls} of {func.__name__!r}')
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls