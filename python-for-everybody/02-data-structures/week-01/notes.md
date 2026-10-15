# 02-data-structures - Week 1

## Τι έμαθα

## Παράδειγμα κώδικα


                                                            **Thursday 15/10/2026 **

Strings in Python, focusing on how to manipulate and work with them effectively.
You cannot directly add integers to strings; conversion functions like int() are used to convert strings to numbers for arithmetic operations.

#Indexing and Accessing Characters

Strings are indexed starting at 0, meaning the first character is at position 0. The index operator (square brackets) allows access to individual characters by their position, e.g., fruit[1] gives the second character (r)
Accessing an index outside the string length results in an IndexError.  
The position inside the brackets is called the index.
Indexing starts at 0, so the first character is at index 0, the second at index 1, and so on.
Example: If fruit = "banana", then fruit[1] gives 'a' (the second character).
The expression inside the brackets can be a constant, variable, or any expression that evaluates to an integer. This operator lets you retrieve specific characters from a string based on their position.


#Looping Through Strings

You can loop through strings using a while loop with an index variable or more simply with a for loop that iterates over each character directly.
The for loop is preferred for its simplicity and readability.

#String Slicing
slicing lets you pick a start point and an end point to grab a part of the string.
For example, if you have the word "Pythonista" and you want to get just "Pyth", you can use slicing like this:

word = "Pythonista"
slice_part = word[0:4]
print(slice_part)

Here’s what’s happening:
word[0:4] means start at position 0 (the first letter 'P') and go up to but not including position 4.
So it grabs letters at positions 0, 1, 2, and 3, which are 'P', 'y', 't', and 'h'.
The result is "Pyth".