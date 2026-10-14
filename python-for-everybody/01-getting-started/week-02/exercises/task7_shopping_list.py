#Shopping list (lists, dictionaries, .items())
#Create a dictionary of 4 items and their prices.
#Loop through it and print each item with its price. Then ask the user for an item name and print its price, or “Not found”.

items={
    "butter":1.5,
    "bread":1.0,
    "cheese":3.5,
    "yogurt":2.0
    }

for item, price in items.items():
    print(item, price)

name=input("Item name: ").lower()
if name in items:
    print(items[name])
else:
    print("Not found")