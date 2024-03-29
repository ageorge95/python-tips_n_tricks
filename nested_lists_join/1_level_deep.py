list_a = [[1, 2, 3], [4, 5, 6]]


# will join the nested lists of a list into a simple list
print([j for i in list_a for j in i])


# equivalent to
final_list = []

for i in list_a:
    for j in i:
        final_list.append(j)

print(final_list)

# OR you can use this syntax sugar (but only for a known list_a length)
print([*list_a[0], *list_a[1]])