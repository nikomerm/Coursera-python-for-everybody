# Build a Number Pattern Generator
# In this lab you will practice the basics of Python by building a small app that creates a number pattern.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a function named number_pattern that takes a single parameter n (representing a positive integer).
# number_pattern should use a for loop.
# number_pattern(n) should return a string containing all integers from 1 through n, inclusive, separated by spaces. 
# For example, number_pattern(4) should return the string 1 2 3 4.
# If the argument passed to the function is not an integer value, the function should return Argument must be an integer value.
# If the argument passed to the function is less than 1, the function should return Argument must be an integer greater than 0.

# Tests:
# Waiting:1. You should have a number_pattern function.
# Waiting:2. The number_pattern function should have one parameter named n.
# Waiting:3. number_pattern(4) should return 1 2 3 4.
# Waiting:4. number_pattern(12) should return 1 2 3 4 5 6 7 8 9 10 11 12.
# Waiting:5. number_pattern should return a space-separated list of numbers for any positive integer.
# Waiting:6. number_pattern should return Argument must be an integer value. when passed a value that is not an integer.
# Waiting:7. number_pattern should return Argument must be an integer greater than 0. when passed a non-positive integer.



def number_pattern(n):
    if not isinstance(n, int): 
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    lst = []
    for i in range(1, n + 1):
        lst.append(str(i))
    return " ".join(lst)
 
print(number_pattern(4))
print(number_pattern(12)) 