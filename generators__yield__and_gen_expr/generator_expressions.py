# You can use () to create a generator with NO memory penalty; Much better than a list comprehension [].
# BUT list comprehensions are faster than generators; So if memory is not an issue list comprehension is better.

# will create a usual list comprehension
nums_squared_lc = [num ** 2 for num in range(5)]

# will create a generator
nums_squared_gc = (num ** 2 for num in range(5))

print(nums_squared_lc)
print(nums_squared_gc) # will print the generator obj
print([_ for _ in nums_squared_gc]) # will print the data within the generator