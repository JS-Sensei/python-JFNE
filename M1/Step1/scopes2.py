# Local versus Global 2

def local(): 
    # m doesn't belong to the scope defined by the local function
    # so python will keep looking into the next enclosing scope.
    # m is finally found in the global scope
    print(m, 'Printing from the local scope')

m = 5
print(m, 'printing from the global scope')
local()