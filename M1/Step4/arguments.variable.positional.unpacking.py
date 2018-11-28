def func(*args):
    print(args)

values = (1, 3, -7, 9)
func(values) # equivalent to: func((1, 3, -7, 9))
func(*values) # equivalent to: func(1, 3, -7, 9)

# Calling the function with something else
func((1, 2, 3), ['a', 'b', 'c']) # ((1, 2, 3), ['a', 'b', 'c'])
