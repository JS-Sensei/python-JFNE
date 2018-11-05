items = [0, None, 0.0, True, 0, 7] # True and 7 evaluate to True
found = False # This is a flag using the flag pattern

for item in items:
    print('Scanning Item', item)
    if item:
        found = True # We update the flag
        break # Break completely outta the loop

if found:
    print('At least one item evaluates to True')
else:
    print('All items evaluate to False')