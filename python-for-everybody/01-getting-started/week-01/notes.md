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