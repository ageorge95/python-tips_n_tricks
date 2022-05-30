list_a = [[[1, 2, 3]], [[4, 5, 6]]]

# will join the nested lists of a list into a simple list
print([x for i in list_a for j in i for x in j])


# equivalent to
final_list = []

for i in list_a:
    for j in i:
        for x in j:
            final_list.append(x)

print(final_list)