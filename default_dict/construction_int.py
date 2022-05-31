# Using an int when constructing a default dict means that all values will be treated as a int, default 0

from collections import defaultdict

# Defining the dict
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count

for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    print(f"before {i}", d[i])
    d[i] += 1
    print(f"after {i}", d[i])

print(d)
print(d[5])