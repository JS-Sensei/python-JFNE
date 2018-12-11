from math import sqrt

# this will generate all possible pairs
mx = 10
legs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]

# this will filter out all non pythagorean triple
filtered_legs = list(
    filter(lambda triple: triple[2].is_integer(), legs)
)
print(filtered_legs)