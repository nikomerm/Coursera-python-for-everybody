#Task 6: Nested conditions
#Ask for the user’s age, then ask whether they have a ticket (yes or no).
# If the age is 18 or more, check the ticket: print Welcome if yes, Buy a ticket if no. If under 18, print Not allowed


age = int(input("Enter your age:"))
ticket = input("Do you have a ticket? Type: yes or no :")

if age >= 18:
    if ticket == "yes":
        print("Welcome")
    else:
        print("Buy a ticket")
else:
    print("Not allowed")

    