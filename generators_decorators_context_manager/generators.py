import sys
import cProfile
# Keyword is yield, this makes a generator


########################################################################################################################
# Generators vs list example

nums_squared_lc = [num**2 for num in range(10000)]  # List comprehension
nums_squared_gc = (num**2 for num in range(10000))  # Generator comprehension

def generator_memory():
    print('Showing the memory reserved by a list and a generator\n')
    print('The size of list: ', sys.getsizeof(nums_squared_lc), ' bytes')
    print('the size of generator: ', sys.getsizeof(nums_squared_gc), ' bytes')

# Generators for optimizing memory
# If the list is smaller than the running machine’s available memory, then list comprehensions can be faster to evaluate.

def profiling():
    print('Showing the numbers of function calls in each list, and the time it takes')
    print('Running a list:')
    cProfile.run('sum([num**2 for num in range(10000)])')
    print('Running a generator: ')
    cProfile.run('sum((num**2 for num in range(10000)))')



########################################################################################################################
# Pythons yield statement
# This is a characteristic for a generator
# yield controls the flow of a generator function, similar to return, but doesn't exit the code.

def yield_presentation():
    yield_str = "This is the first string"
    yield yield_str
    yield_str = "This is the second string"
    yield yield_str
    yield_str = "This is the second string"
    yield yield_str


#Using next on yield strings showing a stop iteration
demo_of_yield = yield_presentation()
print(next(demo_of_yield))
print(next(demo_of_yield))
print(next(demo_of_yield))
#print(next(demo_of_yield)) # produces a StopIteration exception
