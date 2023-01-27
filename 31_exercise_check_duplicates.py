# Exercise: Check for duplicates in list:

some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for item in range(len(some_list)):
    for x in range(item+1,len(some_list)):
        if some_list[item] == some_list[x]:
            duplicates.append(some_list[item])

print(duplicates)

# alternate solution:

duplicates1 = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates1:
            duplicates1.append(value)

print(duplicates1)