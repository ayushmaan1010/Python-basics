# map(action,data)
# action: can be a function
# data: any iterable like, list, tuple, etc.
# map returns a map object.

my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0

# Filter: Return an iterator yielding those items of iterable
# for which function(item) is true.
# If function is None, return the items that are true.
print(list(filter(only_odd, my_list)))

# Map: Make an iterator that computes the function 
# using arguments from each of the iterables. 
# Stops when the shortest iterable is exhausted.
print(map(multiply_by_2, my_list))  # run function on each item

# outputs map object as a list
print(list(map(multiply_by_2, my_list)))

# no change in original list
print(my_list)

# above function code is equivalent to following code:
# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by_2([1, 2, 3]))
