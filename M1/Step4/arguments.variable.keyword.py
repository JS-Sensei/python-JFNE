def func(**kwargs):
    # the ** operator tells the function that it should exepect a variable
    # number of keyword arguments and that they should be stored in a 
    # dictionnary
    print(kwargs)

func(a=1, b=42) #{'a': 1, 'b': 42}
func(**{'a': 1, 'b': 42}) # {'a': 1, 'b': 42}
func(**dict(a=1, b=42)) # {'a': 1, 'b': 42} unpack the dictionnary to send the pair of key values as keyword arguments to the function