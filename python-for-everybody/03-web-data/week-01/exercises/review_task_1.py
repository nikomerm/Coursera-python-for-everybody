# Task 1: Parse JSON and calculate

# Trains: json.loads, list of dicts, for loop

# python
# orders = '[{"id":1,"item":"Book","price":12.5,"qty":2},{"id":2,"item":"Pen","price":1.2,"qty":10},{"id":3,"item":"Bag","price":30,"qty":1}]'

# Write total_revenue(orders_json, min_total):

# Convert the string to Python data.
# Loop through the orders. The total of one order is price * qty.
# Add it up only if the order total is >= min_total.
# Return the sum.

# Expected: total_revenue(orders, 20) gives 55.0, and total_revenue(orders, 0) gives 67.0.

import json

orders = '[{"id":1,"item":"Book","price":12.5,"qty":2},{"id":2,"item":"Pen","price":1.2,"qty":10},{"id":3,"item":"Bag","price":30,"qty":1}]'

def total_revenue(orders_json, min_total):
    info = json.loads(orders_json)
    total = 0
    for item in info:
        cost = item['price'] * item['qty']
        if cost >= min_total:
            total = total + cost
    return total

print(total_revenue(orders, 20))   # 55.0
print(total_revenue(orders, 0))    # 67.0

    

    


