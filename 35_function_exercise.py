# Write a function to return highest even number from a list

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


li = [2, 4, 6, 8, 3, 10, 23, 22, 11]
print(highest_even(li))
