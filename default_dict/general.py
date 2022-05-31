from collections import defaultdict

# Function to return a default values for keys that is not present
# The def_value() method dictates what value is returned if the key is not present in the default dict.
def def_value():
    return "Not Present"

# Defining the dict
d = defaultdict(def_value)
d["a"] = 'value_a'
d["b"] = 'value_b'

print(d["a"])
print(d["b"])
print(d["c"])