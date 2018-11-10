# Implementing the Switch Statement in Python
day_Number = input('Give the Day number which should be comprised between 0 and 6: ')

if 1 <= day_Number <= 5:
    day = 'Weekday'
elif day_Number == 6:
    day = 'Saturday'
elif day_Number == 0:
    day = 'Sunday'
else:
    day = ''
    raise ValueError(str(day_Number) + ' is not a valid day number.')