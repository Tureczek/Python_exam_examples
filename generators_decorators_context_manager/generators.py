import sys
import cProfile

# yield
########################################################################################################################
# Generators vs list example

nums_squared_lc = [num ** 2 for num in range(10000)]  # List comprehension
nums_squared_gc = (num ** 2 for num in range(10000))  # Generator comprehension


def generator_memory():
    print('Showing the memory reserved by a list and a generator\n')
    print(f'The size of list: {sys.getsizeof(nums_squared_lc)} bytes')
    print(f'The size of generator: {sys.getsizeof(nums_squared_gc)}  bytes')


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
    yield_str = "This is the third string"
    yield yield_str


# Using next on yield strings showing a stop iteration
demo_of_yield = yield_presentation()


# print(next(demo_of_yield))
# print(next(demo_of_yield))
# print(next(demo_of_yield))
# print(next(demo_of_yield)) # produces a StopIteration exception


def infinite_count():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_count()

# print(next(gen))

########################################################################################################################
# Creating palindrome function and using advanced methods

def is_palindrome(num):
    if num // 10 == 0:  # // = Floor division - rounds down to a full integer.
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


'''
for i in infinite_count():
    pal = is_palindrome(i)
    if pal:
        print(pal)
'''


def is_palindrome2(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindrome():
    num = 0
    while True:
        if is_palindrome2(num):  # With python 2.5 yield was introduced as an expression rather than a statement.
            i = (yield num)  # But can still be used as an expression as shown in yield_presentation().
            if i is not None:  # This could happen if next() is called on the generator object.
                num = i
        num += 1


def adv_throw():
    pal_gen_throw = infinite_palindrome()
    for i in pal_gen_throw:
        print(i)
        digits = len(str(i))
        if digits == 10:
            pal_gen_throw.throw(ValueError("No palindromes larger than 10 in length"))
        pal_gen_throw.send(10 ** (digits))


def adv_close():
    pal_gen_close = infinite_palindrome()
    for i in pal_gen_close:
        print(i)
        digits = len(str(i))
        if digits == 10:
            pal_gen_close.close()
        pal_gen_close.send(10 ** (digits))


########################################################################################################################
# Using Generators as a data pipeline

'''
 -   Read every line of the file.
 -   Split each line into a list of values.
 -   Extract the column names.
 -   Use the column names and lists to create a dictionary.
 -   Filter out the rounds you aren’t interested in.
 -   Calculate the total and average values for the rounds you are interested in.
'''


def data_pipeline():
    file_name = 'techcrunch.csv'
    lines = (line for line in open(file_name))  # Generator expression
    list_line = (s.rstrip().split(',') for s in lines)  # iterates through generator lines
    cols = next(list_line)  # pass first column

    company_dicts = (dict(zip(cols, data)) for data in list_line)  # Creating a dict

    funding = (
        int(company_dicts['raisedAmt'])
        for company_dicts in company_dicts
        if company_dicts['round'] == 'a'
    )

    print('\n'.join([str(i) for i in company_dicts]))

    total_series_a = sum(funding)
    print(f'Total series A fundraising: ${total_series_a}')

########################################################################################################################
