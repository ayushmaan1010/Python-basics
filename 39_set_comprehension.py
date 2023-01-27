# Set comprehension

# for a unique variable char iterating over 'hello' add it to my_set
my_set = {char for char in 'hello'}
# for a variable num iterating on range 1 to 10 add it to my_set1
my_set1 = {num for num in range(1, 11)}

print(my_set)
print(my_set1)

# Dictionary comprehension

my_list = [1, 2, 3]
my_dict = {num: num*2 for num in my_list}

print(my_dict)
