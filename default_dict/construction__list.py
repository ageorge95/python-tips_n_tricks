# Using a list when constructing a default dict means that all values will be treated as a list, default []

from collections import defaultdict

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)