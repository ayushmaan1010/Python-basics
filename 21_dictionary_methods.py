user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}
# get(key,value):if age exist print it, else create age and assign 55 to it
print(user.get('age', 55))

user2 = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
# get(key,value):if age exist print it, else create age and assign 55 to it
print(user2.get('age', 55))

print('age' in user.keys())  # checks if age is in keys of user
print("hello" in user.values())  # checks if hello is in values of user
print(user.items())  # outputs dictionary as a tuple
user.clear() # clear dictionary
print(user)
user2.update({'age':45})
print(user2['age'])