# Sets: unordered collections of unique objects

my_set = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}
print(my_set)  # only returns the unique items
my_set.add(100)
my_set.add(1)
print(my_set)  # only 100 gets added as it is not present in my_set.

my_list = [1, 2, 3, 4, 5, 5]
# convert my_list to a set
print(set(my_list))

print(len(my_set))
print(5 in my_set)
