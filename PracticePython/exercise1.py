'''
Exercise 1
 Create a program that asks the user to enter their name and their age. 
 Print out a message addressed to them that tells them the year that they will turn 100 years old.

 Extras: 
 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
 2. Print out that many copies of the previous message on separate lines.

'''
import sys
import datetime

# Take the User age
user_age = int(input('What is your Age? : '))
if user_age < 0:
    print('Your age can\'t be a negative number :p')
    sys.exit(1)
elif user_age > 100 :
    print('You are way too OLD for this.')
else:
    #Now we can work
    # Retrieve the actual Year
    currentYear = datetime.datetime.now().year
    years_to_be_hundred = currentYear + ( 100 - user_age)
    print(years_to_be_hundred)
    print('You will be 100 Years old in %d'%years_to_be_hundred)

