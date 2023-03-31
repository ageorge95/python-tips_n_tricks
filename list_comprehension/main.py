initial_list = [1,2,3,4,5,6]

# quickly check if elements are meeting a certain condition
list_comprehension = [_ > 3 for _ in initial_list]
print(list_comprehension)

# quickly filter elements
list_comprehension = [_ for _ in initial_list if _ > 3]
print(list_comprehension)

# combined quick filter and condition check
list_comprehension = ['higher' if _ > 4 else 'lower' for _ in initial_list if _ > 3]
print(list_comprehension)