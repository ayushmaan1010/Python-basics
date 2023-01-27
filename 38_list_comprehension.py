
# for a variable char iterating over 'hello' add it to my_list
my_list = [char for char in 'hello']
# for a variable num iterating on range 1 to 10 add it to my_list
my_list1 = [num for num in range(1, 11)]
# perform operation on variable num and then add to my_list
my_list2 = [num*2 for num in range(1, 11)]
# only even numbers added to my_list
my_list3 = [num for num in range(1, 11) if num % 2 == 0]

print(my_list)
print(my_list1)
print(my_list2)
print(my_list3)