# A prime Generator

'''
Algorithm to generate prime numbers:
A prime number( or a prime) is a natural number greater than 1 that has no
positive divisors other 1 and itself. A natural number greater than 1 that 
is not a prime number is called a composite number. 
'''

primes = [] # THis will contain the primes in the end
upto = 100 # the limit, inclusive 
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break # Stop the inner for loop
    else: 
        primes.append(n)

print(primes)