people = ['Jonas', 'Julio', 'Mike', 'mez']
ages = [25, 30, 31, 39]

for position in range(len(people)): 
    person = people[position]
    age = ages[position]
    print(person, age)

# More pythonic Way of doing it
print('Now a more pythonic way to do it but still less optimal')
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

#  THe pythonic way in itself
for person, age in zip(people, ages): 
    print(person, age)

# Adding nationalities to the mix
print('Addinig Nationalities to the mix')
nationalities =  ['Belgium', 'Spain', 'England', 'Bangladesh']
for data in zip(people, ages, nationalities):
    print(data)
    # And you can explode it like
    person, age, nationality = data
    print('Person: ',person, ' is ',age, ' years old and comes from ',nationality)

