# Generators  can be seen as python functions BUT the function that created them does not exit after that function is called. For example:
#
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
# This looks like a typical function definition, except for the Python yield statement and the code that follows it.
# yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.
# Instead, the state of the function is remembered. That way, when next() is called on a generator object
# (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again.
# Since generator functions look like other functions and act very similarly to them,
# you can assume that generator expressions are very similar to other comprehensions available in Python.

my_list = [1, 2, 3, 4, 5]


def return_my_list_usually():
    return [x for x in my_list]

def return_my_list_yield():
    for x in my_list:
        yield x

print(return_my_list_usually())

my_list_as_generator = return_my_list_yield()

# read the generator value explicitly
print(next(my_list_as_generator))
print(next(my_list_as_generator))
print(next(my_list_as_generator))
print(next(my_list_as_generator))
print(next(my_list_as_generator))

# read the generator value implicitly
for x in return_my_list_usually():
    print(x)