'''
    Range function showcases:
    you can use the range like this:
    range(limit): generates numbers from 0 to limit-1
    range(start, limit): generates numbers from start to limit-1
    range(start, limit, step): generates numbers from start to limit-1 by 
    step `step`
'''
limit = 25
print('Range with one parameter')
print(list(range(25)))

print('Range with start and stop')
print(list(range(2, limit)))

print('Range With start and stop with step')
print(list(range(0, limit, 5)))