#Tip calculator (variables, input, f-strings)
#Ask for a bill amount and a tip percentage. Print the tip and the total, rounded to 2 decimals.

print("Welcome to tip calculator mini program!\n")

bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter a tip percentage: "))
tip = (bill_amount * (tip_percentage / 100))
total = tip + bill_amount

print(f"The tip is: {tip:.2f}")
print(f"The total is: {total:.2f}")

