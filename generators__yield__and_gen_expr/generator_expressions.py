# will create a usual list comprehension
nums_squared_lc = [num ** 2 for num in range(5)]

# will create a generator
nums_squared_gc = (num ** 2 for num in range(5))

print(nums_squared_lc)
print(nums_squared_gc) # will print the generator obj
print([_ for _ in nums_squared_gc]) # will print the data within the generator