
# Define The Class a simple class Person with only one data
class Person: 
    def __init__(self, age): 
        self.age = age
    

# Create an  instance of the class
fab = Person(age=39)
print('Fab age is: ', fab.age)
print('Fab variable id is',id(fab))

fab.age = 29
print('Fab age is: ', fab.age)
print('Fab variable id is', id(fab))
