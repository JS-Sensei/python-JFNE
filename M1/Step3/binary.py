n = 6
remainders = []
while n > 0:
    remainder = n % 2 # Remainder of division by 2
    remainders.append(remainder) # we keep track of remainders
    n //= 2 # Equals n = n // 2
# Reassign the list to its reversed copy and print it
remainders.reverse()
print(remainders)