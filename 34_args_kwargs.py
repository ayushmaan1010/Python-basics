# *args **kwargs
# *args: function can take any number of positional arguments like this
# **kwargs: add keyword args
def super_func(*args):
    print(*args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))
