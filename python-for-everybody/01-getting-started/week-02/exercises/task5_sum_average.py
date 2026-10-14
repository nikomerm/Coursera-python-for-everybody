#Sum and average (while loop, “done”, try/except)
#Repeatedly ask for numbers until the user types “done”. Print the count, total, and average. Ignore bad input, and handle the case where no numbers were entered.

count = 0
total = 0

while True:
    text = input("Enter a number or type 'done': ")
    if text == "done":
        break
    try:
        number = int(text)
    except ValueError:
        print("Invalid input")
        continue
    count = count + 1
    total = total + number

if count == 0:
    print("No numbers entered")
else:
    average = total / count
    print("Count of numbers:", count)
    print("Total of numbers:", total)
    print("Average of numbers:", average)




