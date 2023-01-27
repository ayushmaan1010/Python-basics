basket = [1, 2, 3, 4, 5]

# adding
basket.append(10)  # add an element at the last
print(basket)
basket.insert(5, 6)  # add an element at an index
print(basket)

# removing
basket.pop()  # pop off element at the end
print(basket)
basket.pop(3)  # pop off element at the index 3
print(basket)
basket.remove(1)  # remove item '1'
print(basket)

print(basket.count(3))  # count occurances of an object in list
print(5 in basket)  # returns true if item present else false

elements = [234, 5, 242, 2, 23, 4, 2, 4, 24]
elements.sort()
print(elements)
elements.reverse()
print(elements)

print(list(range(11)))
