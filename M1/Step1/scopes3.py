# Local, Enclosing and Global
def enclosing_func(): 
    m = 13
    def local():
        # m doesn't belong to the scope defined by the local function
        # so ypthon will look for it in the enclosing scope which is the scope
        # defined by the `enclosing_func`
        print(m, 'Printing from the local scope')
    # Calling the function local
    local()
m = 5

print(m, 'Printing from the Global Scope')

enclosing_func()