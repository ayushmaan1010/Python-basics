# scope - what variables do I have access to?

a = 1


def confusion():
    a = 5
    return a


print(a)  # print value of global variable 'a'
print(confusion())  # print value of local variable 'a'


# scope rules/order:
# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - built in python functions.

# Rules for pure function:
#     return same output everytime
#     doesn't effect anything outside its scope

# pure function: makes code less buggy and more readable.
# pure function not always possible. They are the ideal case.
