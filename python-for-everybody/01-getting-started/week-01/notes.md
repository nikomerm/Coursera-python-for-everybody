# 01-getting-started - Week 1

## Τι έμαθα

## Παράδειγμα κώδικα

                                        **Δευτέρα 05/10/2026**
Τελείωσα το "Module 1- Chapter One Why We Program" , Lecture 1 Chapter 1
Module 1 and Lecture 1 of Chapter 1 focus on introducing the basics of programming and the Python language. Παρακάτω μερικά χρήσιμα notes:

~Introduction to Programming and Python
Programming involves writing instructions for computers to perform tasks.
Why We Program : Programming helps solve problems and automate tasks.
Python = Guido van Rossum - Python comes from Monty Python Flying Circus and not the Snake PYTHON
syntax error and what it means --> python is LOST ~

                                        **Τρίτη 06/10/2026**
Module 4: Chapter Two - Variables and Expressions

Constants -> fixed values (numbers,letters and strings) value that does not change example:123, 'Hello World'
Variables: ALWAYS start with a letter or undescore _ . Examples: speed, _speed
            Wrong Variables: 23speed, #speed, speed.123
Assignments Statements
(=) An assignment statement consists of an expression on the Right-hand side and variable to STORE the result
    example: x = [3,9 * x * (1-x)]--->[computes the expression and then puts in variable x]
A Variable is a memory location used to store a value. The Right side is an expression, once the expression is evaluated, the result is placed in (assigned to) x.
ORDER OF EVALUATION: "operator precedence" --> wich operator "takes precedence" over others.
    example: 1 + 2 * 3 - 4 / 5 ** 6        or       1 + (2 * 3) - (4 / (5 ** 6)) 
Rule : 1. Parenthesis -> 2. Power -> 3. Multiplication -> 4. Addition -> 5. Left to Right
Modulo Expression -- REMAINDER OPERATOR % Example -> 42 % 10 = 2 -> Devide the number: 42 / 10 = 4
                                                                    Multiply to check: 10 times 4 is 40
                                                                    Substruct to find what is left: 42 - 40 = 2
                                                                    
                                    **Τετάρτη 07/10/2026**
Variables Types: type() function -> to ask python what type something is.
USER INPUT: input() function -> python reads data from the user and the input() function returns a string.
#comments: # -> for describing what is going to happen in a sequence of code, # -> to turn off a line of code perhaps temporarly
Pattern that computers do : Input --> Processing --> Output

                                    **Πέμπτη 08/10/2026**
Conditional statments: Boolean expressions -> ask a question and produce a Yes or No result -> using Comparison oparators evaluate True/False or Y/N
 < Less than
 <= Less than or Equal to
 == Equal to -> ? . = assignment statement x=1. x==1 means -> is x equals to 1 ??????? (Ερώτημα)
 >= Greater than or Equal to
 > Greater than
 != Not Equal
None of these harm the data that they are looking at. They evaluate and they return a True or False

indetation = 4 spaces or 1 tab key. Indetation controls the flow of the execution in conditional blocks

Sequencial code -> Sequential code is code that runs line-by-line, from top to bottom, in the exact order it is written. 
# Example of Sequential Code
x = 10
y = 5
total = x + y
print(total)  # This will always print 15

Conditional code -> Conditional code allows a program to choose between different paths based on whether a condition is true or false.
# Example of Conditional Code
age = 20

if age >= 18:
    print("You are an adult.")  # Runs ONLY if age is 18 or older
else:
    print("You are a minor.")   # Runs ONLY if age is less than 18

Nested code -> Nested code occurs when you place one control structure inside another control structure (block with in a block).
# Example of Nested Code
has_ticket = True
baggage_cleared = False

if has_ticket:  # Outer condition
    print("Welcome to security.")
    
    if baggage_cleared:  # Inner / Nested condition
        print("You may board the plane.")
    else:
        print("Baggage failed. You cannot board.")
        
else:
    print("You cannot enter the airport.")

two way decisions -> Else

                                    **Παρασκευή 09/10/2026**
review day, asked claude to make tasks on what i did the previous days in order to practice.

                                    **Σάββατο 10/10/2026**
Using functions: 
Pattern for code: Sequencial, Conditional, Iterations(επαναλήψεις), Store & Reuse.
Functions are those things that store and reuse. They are like variables, but they hold - store the code.

function needs to be called in order to execute. When you define, you need to call it (re-use).
Difference between Parameters and Arguments.  Parameters are the variable names defined function definition. They act as placeholders for the values the function will receive.   Arguments are the actual values you pass into the function when you call it. Example:
def greet(name): # name is a parameter
    print("Hello", name) . When you call greet("Sally") the string "Sally" is the argument. Parameters are like empty boxes in the function waiting to be filled and arguments are the items you put into those boxes when you use the function.
Return Values: return -> stops the function, -> determines the residual(υπόλοιπο) value.
Some functions do not return values -> Non Fruitful functions, and if they return values they called Fruitful functions.

Extra realization while doing excercises ----->>>>

 Calling a function just means writing its name with parentheses: square(4). That alone runs it. print is a separate step you add only if you want to see a value. What you do next depends on what the function does:

greet()                 # just call it: it performs an action (prints) itself

result = square(4)      # call it and store the returned value for later

print(square(4))        # call it and show the returned value right away

if is_adult(20):        # call it and use the returned value in a decision
    print("Welcome")


Extra realization while doing excercises no2 ----->>>>

                                                  A METHOD TO TRY ON EVERY TASK

Underline what the function receives (parameters).

Underline what it produces (return) or shows (print).

Underline what the main program does: ask the user, call, store, print.

Write the three parts in order: definition, input, call.

Phrase translator

The task says	It means
“Write a function called f that takes X and Y” ----> It means:	def f(x, y):

“The function should return...” ----> It means:	return inside it

“The function should print...” ----> It means:	print inside it

“Call the function with 5 and 7” ----> It means:	f(5, 7)

“Call the function and print the result” ----> It means:	print(f(5, 7))

“Call the function and store the result” ----> It means:	result = f(5, 7)

“Use the user’s input as the argument” ----> It means:	f(user_value), after input() and conversion

                                **Κυριακή 11/10/2026**
 Indefinite loops ----> "while loops," which are a way to tell a computer to repeat a task over and over as long as a certain condition is true.
 Υou start with a condition, like "while n is greater than 0." Inside the loop, you do something, like print the number and then subtract 1 from it. The loop keeps going, checking the condition each time, until the condition becomes false (n is no longer greater than 0). This way, the loop knows when to stop.
 An iteration variable in a while loop is a variable that changes its value each time the loop runs (each iteration). It controls how many times the loop will execute by affecting the loop's condition.
 For example, if you have a variable n starting at 5, and your loop says "while n > 0," the iteration variable n is decreased by 1 each time through the loop. This change eventually makes the condition false (when n reaches 0), so the loop stops.
Without an iteration variable that changes, the loop might run forever because the condition never becomes false.
Here's the difference between break and continue in loops:

break: Immediately stops the entire loop and moves to the code right after the loop. It's like saying, "Stop everything and exit the loop now."

continue: Skips the rest of the current loop iteration and goes back to the start of the loop to check the condition again. It's like saying, "Skip this round and start the next one."

Example:
Use break when you want to exit the loop early based on a condition.
Use continue when you want to skip some steps in the current iteration but keep looping.

Definite loops ---> "for loops". Understanding the For Loop: A Beginner-Friendly Explanation

Imagine you have a list of your favorite fruits, and you want to say "I love [fruit]" for each one. Instead of repeating the sentence for every fruit manually, you can use a for loop in Python to do it for you automatically. A for loop is like a helpful assistant that goes through each item in a collection (like your list of fruits) one by one and performs the same action for each item.

In Python, the for loop looks like this:

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print("I love", fruit)
Here’s what’s happening:

fruits is your list of items.

fruit is a temporary name for each item as the loop goes through the list. Here, "fruit" is the iteration variable. So, the role of "fruit" is to represent the current item from the list during each loop cycle, allowing you to work with that item inside the loop. It's like a placeholder that changes its value each time the loop repeats.

The loop runs once for each fruit, printing "I love apple," then "I love banana," and finally "I love cherry."
This way, the for loop helps you repeat tasks easily and clearly without writing repetitive code. It’s like telling Python, "For each thing in this group, do this action."

Another example: What is the largest number?
numbers = [3, 7, 2, 9, 5]
largest = numbers[0]  # Start with the first number

for num in numbers:
    if num > largest:
        largest = num  # Update largest if current number is bigger

print("The largest number is:", largest)  

Here's how it works step-by-step:

Initially, largest is set to the first number, 3.
The loop checks the next number, 7. Since 7 > 3, it updates largest to 7.
Then it checks 2. Since 2 is not greater than 7, largest stays 7.
Next, it checks 9. Since 9 > 7, it updates largest to 9.
Finally, it checks 5. Since 5 is not greater than 9, largest stays 9.
After going through all numbers, largest holds the value 9, which is the biggest number in the list.


**Counting, totaling, and filtering in loops:**

**Counting:** First, counting is like keeping track of how many fruits you have. You start with zero and add one each time you look at a fruit. In code, you set a variable to zero before the loop starts, then add one inside the loop for each item you see. This helps you know how many times the loop ran.
**Totaling:** next, totaling is like adding up the weight of each fruit. You start with zero and add the weight of each fruit as you go through the basket. In code, you have a variable for the total, start it at zero, and add each value inside the loop. This way, you get the sum of all the values.
**Filtering:** Finally, filtering is like checking each fruit to see if it meets a condition, such as being heavier than 20 grams. If it does, you do something special with it, like picking it out or noting it. In code, you use an "if" statement inside the loop to check the condition and act accordingly.

Example: 
# List of numbers to process
numbers = [9, 41, 12, 3, 74, 15]

# 1. Counting the number of items
count = 0
for num in numbers:
    count = count + 1
print("Count of numbers:", count)

# 2. Totaling the values
total = 0    
for num in numbers:
    total = total + num
print("Total of numbers:", total)

explanation ## Initializing total to zero before the loop is important because it sets a starting point for the accumulation. Think of total as a container that holds the sum as you add each number from the list.
If you didn't initialize total to zero, Python wouldn't know what value to start with, and you would get an error because you would be trying to add a number to something that doesn't exist yet. without defining total first, Python would raise a NameError saying that total is not defined.
So, initializing total = 0 ensures that you have a valid starting value to add numbers to.

# 3. Calculating the average
# Using count and total from above
average = total / count
print("Average of numbers:", average)

# 4. Filtering: print numbers greater than 20
print("Numbers greater than 20:")
for num in numbers:
    if num > 20:
        print(num)

# 5. Using a Boolean flag to check if a specific number (3) is found
found = False
for num in numbers:
    if num == 3:
        found = True
        break  # Optional: stop loop once found
print("Is number 3 found?", found)

Finding the Smallest Value

Simply changing the comparison from "greater than" to "less than" and renaming variables is not enough to find the smallest value correctly.
Starting with an initial smallest value like -1 or a large number can cause errors, especially if the list contains only positive or negative numbers.
Using None as a Flag Value

The solution is to initialize the smallest value variable to None, which represents the absence of a value.
During the first iteration, if the smallest value is None, the current number is assigned as the smallest.
For subsequent iterations, the code compares the current number to the smallest and updates it if the current number is smaller.
Loop and Logical Operators
The "is" and "is not" operators are used to check if a variable is None, which is a stronger form of equality than "==".
This technique of using None as a flag is useful for initializing loop variables when searching for minimum or maximum values.

numbers = [9, 41, 12, 3, 74, 15]

smallest = None
for value in numbers:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value

print("Smallest value is:", smallest)