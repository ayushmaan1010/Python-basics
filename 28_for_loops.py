# Loops: execute a part of code again and again

# for variable in iterable:
#   do something

# iterables: collection of items, such as, list, set, tuple, strings, dictionary
# iterated: one by one check each item in the collection.
for item in 'hello world':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in [1, 2, 3]:
    for x in ['a', 'b']:
        print(item, x)

# iterating over dictionaries:
user = {
    'name': 'Yami',
    'age': 40,
    'is_captain': True
}

for item in user.items(): # display (key, value) as a tuple
    print(item)

for item in user.values(): # display values only
    print(item)

for item in user.keys(): # display keys only
    print(item)

for key,value in user.items(): # key in variable key and value in value
    print(key,value)

