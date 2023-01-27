# TUple : immutable lists
my_tuple = (1, 2, 3, 4, 5, 5, 4, 7, 2, 3, 4, 2, 5, 3)
# my_tuple[1] = 'z' #produces error

print(my_tuple[1])  # outputs 2
# whenever we want a list that doesn't need to be changed we use tuple.
# Tuples are faster than lists.
print(my_tuple[1:3])
x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(other)
print(my_tuple.count(5))  # count number of occurances of an item
print(my_tuple.index(5))  # return first index of a value
