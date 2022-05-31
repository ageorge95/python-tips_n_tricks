# NOTE: same logic as in default_dict/general.py, but simplified, using lambda

from collections import defaultdict

# Defining the dict and passing
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 'value_a'
d["b"] = 'value_b'

print(d["a"])
print(d["b"])
print(d["c"]) 