#Task 4: Modulo
#Ask the user for a whole number and print whether it is even or odd. Hint: what does % 2 give you in each case?

number=input("enter number:")
n=int(number)
if n % 2 == 0:
    print("number is even")
else:
    print("number is odd")