x = [1, 2, 3]

def func(x):
    print('Inside func modifying the array')
    x[1] = 42 #this affects the caller

func(x)
print(x)