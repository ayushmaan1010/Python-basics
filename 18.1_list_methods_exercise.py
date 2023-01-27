# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket

basket.remove('Banana')
print(basket)

basket.remove('Blueberries')
print(basket)

basket.append('Kiwi')
print(basket)

basket.insert(0,'Apples')
print(basket)

print(basket.count("Apples"))

basket.clear()
print(basket)