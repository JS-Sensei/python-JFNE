def func(a=[], b={}):
    print(a)
    print(b)
    print('#'*12)
    a.append(len(a)) # this will affect a'S default value
    b[len(a)] = len(a) # and this will affect b's one 

func() # a=[], len(a) = 0, a=[0], len(a)=1, b = {1: 1}
func() # a=[0], len(a)=1, b = {1: 1}, a=[0, 1], b={1: 1, 2: 2}
func() # same 