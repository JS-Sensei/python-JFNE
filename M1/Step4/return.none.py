def func():
    pass
func() # the return of this call won't be collected It's lost
a = func() # The return of this call is collected in a but it's equal to None
print(a) # prints: None