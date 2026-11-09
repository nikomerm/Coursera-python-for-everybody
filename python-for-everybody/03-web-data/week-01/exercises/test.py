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
    

print(total_revenue(orders, 20))
print(total_revenue(orders, 0))

