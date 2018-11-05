order_total = 247 # GBP

# Classic if/else form:
if order_total > 100:
    discount = 25 # GBP
else:
    discount = 0 #GBP

print(order_total, discount)

# Ternary operator 
discount = 25 if order_total > 100 else 0
print(order_total, discount)