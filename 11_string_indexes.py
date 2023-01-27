# string is stored as an oredered sequence of characters.
# each character including spaces has an index.

a_string = "hello user"
        #   0123456789

print(a_string[0])  # outputs h
print(a_string[6])

# string slicing -> string_name[start (default = 0):end-1 (default n-1):step_over(default = 1)]
print(a_string[1:5])
print(a_string[6:])  # outputs from 6 to end i.e., 'user'
print(a_string[:5])
print(a_string[:])  # whole string

# in python negative means from the end

print(a_string[-1])  # last character
print(a_string[::-1])  # string reverse
