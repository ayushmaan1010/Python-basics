# Dictionary : an unordered key value pair.
# keys must be immutable and unique.
dictionary = {
    'a': 1,
    'b': 2,
    'x': 3
}
print(dictionary)
print(dictionary['b'])

dictionary1 = {
    'a': [1, 2, 3],
    2: True,
    True: 'hello'
}
print(dictionary1)
print(dictionary1[2])
print(dictionary1[True])
