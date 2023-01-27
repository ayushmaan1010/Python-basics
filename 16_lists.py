# list = ordered sequence of objects of any type

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 2.45, 'a', True]

# Data structure = store and access data in a certain manner

amazon_cart = ['notebook',
               'sunglasses',
               'mobile_phone',
               'toys']
print(amazon_cart[1])

# List slicing
print(amazon_cart[0:2])
print(amazon_cart[3:])

# list copying vs list modifying

# amazon_cart gets assigned to new_cart and changes are reflected in it as well
new_cart = amazon_cart
new_cart[0] = 'laptop'
print(new_cart)
print(amazon_cart)

# since slicing produces a copy of the list
# new_cart_1 has a copy of the amazon_cart and changes are done to new_cart_1 only
new_cart_1 = amazon_cart[:]
new_cart_1[1] = 'smartglasses'
print(new_cart_1)
print(amazon_cart)
