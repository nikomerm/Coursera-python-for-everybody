#Number classifier (conditionals, modulo)
#Ask for an integer. Print whether it is positive, negative, or zero, and also whether it is even or odd.

number = int(input("Enter number: "))
if number >= 1:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")