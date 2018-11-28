def outer():
    test = 1 # outer scope

    def inner():
        global test # Accessing test which is in the global scope
        global non_existent #No Error ?!
        test = 2 # global scope
        print('inner: ', test)
    inner()
    print('outer: ', test)

test = 0 # global scope
outer()
print('global: ', test)