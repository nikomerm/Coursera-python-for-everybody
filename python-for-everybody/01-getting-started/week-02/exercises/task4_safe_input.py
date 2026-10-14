#Safe number input (try/except, while, break)
#Keep asking for a number between 1 and 10. On text, print “Invalid input”. On a number outside the range, print “Out of range”. Stop when the input is valid.

while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))
    except ValueError:
        print("Invalid input")
        continue

    if 1 <= number <= 10:
        print(f"Thanks, you entered {number}")
        break
    else:
        print("Out of range")