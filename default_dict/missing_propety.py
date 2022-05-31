from collections import defaultdict

# Defining the dict
d = defaultdict(lambda: "Not Present")
d["a"] = 'value_a'
d["b"] = 'value_b'

# Provides the default value for the key
print(d.__missing__('a'))
print(d.__missing__('d'))