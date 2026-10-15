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

name=input("Item name: ")
if name in items:
    print(items[name])
else:
    print("Not found")




#version no2 same but with fstrings and the use of .lower()
                                                #  What changed:

                                                # The loop prints each pair as butter: 1.50, using :.2f for money.
                                                # The lookup prints a full sentence, with items[name] inside the braces. Any expression works inside { }, not only variables.
                                                # lower() is added on the input, so Cheese now works too.
# items = {
#     "butter": 1.5,
#     "bread": 1.0,
#     "cheese": 3.5,
#     "yogurt": 2.0
# }

# for item, price in items.items():
#     print(f"{item}: {price:.2f}")

# name = input("Item name: ").lower()
# if name in items:
#     print(f"{name} costs {items[name]:.2f}")
# else:
#     print("Not found")