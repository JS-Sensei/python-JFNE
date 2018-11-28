from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)

f5 = factorial(5) # f5 = 120

''' for n = 4 for example we have:
    reduce(mul, range(1, 4+1), 1)
   =reduce(mul, [1, 2, 3, 4], 1)
   =(((1*2)*3)*4) * 1 
'''