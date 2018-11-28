x = [1, 2, 3]

def func(x):
    x[1] = 42 # this changes the caller 
    x = 'Something else' #this points x to a new string object

func(x)
print(x) # Still print: [1, 42, 3]