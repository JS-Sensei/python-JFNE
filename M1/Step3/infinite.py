from itertools import count

for n in count(5, 3): 
    # it starts from 5 and keeps iterating like x_+1 = x + 3
    if n > 20:
        break
    print(n, end=',') # instead of a newline, we put comma and space as the end
