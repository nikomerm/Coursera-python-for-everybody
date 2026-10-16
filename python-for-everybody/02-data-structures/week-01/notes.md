# 02-data-structures - Week 1

## Τι έμαθα

## Παράδειγμα κώδικα


                                                            **Thursday 15/10/2026 **

Strings in Python, focusing on how to manipulate and work with them effectively.
You cannot directly add integers to strings; conversion functions like int() are used to convert strings to numbers for arithmetic operations.

**Indexing and Accessing Characters**

Strings are indexed starting at 0, meaning the first character is at position 0. The index operator (square brackets) allows access to individual characters by their position, e.g., fruit[1] gives the second character (r)
Accessing an index outside the string length results in an IndexError.  
The position inside the brackets is called the index.
Indexing starts at 0, so the first character is at index 0, the second at index 1, and so on.
Example: If fruit = "banana", then fruit[1] gives 'a' (the second character).
The expression inside the brackets can be a constant, variable, or any expression that evaluates to an integer. This operator lets you retrieve specific characters from a string based on their position.


**Looping Through Strings**

You can loop through strings using a while loop with an index variable or more simply with a for loop that iterates over each character directly.
The for loop is preferred for its simplicity and readability.

While loop example:

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

For loop example:

fruit = "banana"
for letter in fruit:
    print(letter)

Both will print each letter of "banana" on a separate line. 


**String Slicing**
slicing lets you pick a start point and an end point to grab a part of the string.
For example, if you have the word "Pythonista" and you want to get just "Pyth", you can use slicing like this:

            word = "Pythonista"
            slice_part = word[0:4]
            print(slice_part)
Here’s what’s happening:
word[0:4] means start at position 0 (the first letter 'P') and go up to but not including position 4.
So it grabs letters at positions 0, 1, 2, and 3, which are 'P', 'y', 't', and 'h'.
The result is "Pyth".



                                                        **Friday 16/10/2026**

**Example of string Type :** 

Email Address as a String

In many data science projects or back-end development tasks, you often work with user data, such as email addresses.
An email address like "john.doe@example.com" is stored as a string type in Python because it is a sequence of characters.
You can manipulate this string to extract useful information, such as the domain name after the "@" symbol.
For instance, using string methods, you can find the position of "@" and slice the string to get "example.com".
This is useful for categorizing users by their email domains or validating email formats.
Why this example is relevant:

It connects directly to the concept of strings as sequences of characters.
It shows how string manipulation (finding characters, slicing) is applied in real-world programming tasks.
It aligns with your interest in back-end development and data science, where handling and processing text data is common.

**String Concatenation with + :**
 Example:

first_part = "Hello"
second_part = "World"
combined = first_part + " " + second_part
print(combined)

**How to check if a substring is inside a string using the --> in <--  operator in Python.**
Example:

fruit = "banana"
if "na" in fruit:
    print("Found 'na' in the fruit!")
else:
    print("'na' not found.")

    **Here's the difference between the ** in ** operator and the ** find() ** method for strings in Python:**

in operator

Checks if a substring exists inside another string.
Returns a Boolean value: True if found, False if not.
Example: "na" in "banana" returns True.

**find() method**

Searches for a substring inside a string.
Returns the index (position) of the first occurrence of the substring.
Returns -1 if the substring is not found.

Example:
 "banana".find("na") returns 2 (the starting index of "na").

--->   Summary:
Use in when you just want to know if the substring exists (True/False).
Use find() when you want to know where the substring is located (index) or if it’s absent (-1).

                                                        **String methods:**
Strings are an example of Python objects. An object contains both data (the actual string itself) and methods, which are effectively functions that are built into the object and are available to any instance of the object.
Python has a function called dir which lists the methods available for an object. The type function shows the type of an object and the dir function shows the available methods.
  {{{ stuff = 'Hello world'
  type(stuff)
  <class 'str'>
>>> dir(stuff)
[... 'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map',
'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)}}}

for more info: https://docs.python.org/library/stdtypes.html#string-methods.

calling a method looks like calling a function (it takes arguments and returns a value) but it has different syntax.
example : >>> word = 'banana'
 >>> new_word = word.upper()
 >>> print(new_word)
 BANANA


**To replace text in a string, you can use the replace() method in Python.**

Example:

greet = "Hello Bob"
new_greet = greet.replace("Bob", "Jane")
print(new_greet)  # Output: Hello Jane
print(greet)      # Original string unchanged: Hello Bob
Explanation:

replace("Bob", "Jane") finds all occurrences of "Bob" in the string and replaces them with "Jane".
It returns a new string with the replacements; the original string stays the same.
You can also replace multiple characters, for example:

new_greet = greet.replace("o", "X")
print(new_greet)  # Output: HellX BXb

**Understanding Stripping Whitespace in Strings**

When we talk about "stripping whitespace" in strings, we're referring to the process of removing extra spaces or invisible characters like tabs or newlines from the beginning and end of a piece of text. Imagine you have a sticky note with a message, but the edges are messy with smudges or extra tape. Stripping whitespace is like cleaning those edges so the message stands out clearly without any clutter around it.

In Python, this is super easy with the strip() method. If you have a string with spaces before or after the actual words, calling strip() on it will give you a clean version without those extra spaces. For example:

text = "   Hello, world!   "
clean_text = text.strip()
print(clean_text)  # Output: "Hello, world!"
Here, the spaces before and after "Hello, world!" are removed, but the words themselves stay intact. This is really helpful when you're working with data from files or user input where extra spaces can sneak in and cause problems.

**Formatted String Literals f -strings**

A formatted string literal (often referred to simply as an f-string) allows Python expressions to be used within string literals. This is accomplished by prepending an f to the string literal and enclosing expressions in curly braces {}.

For example, wrapping a variable name in curly braces inside an f-string will cause it to be replaced by its value:

>>> camels = 42
>>> f'{camels}'
'42'
The result is the string ‘42’, which is not to be confused with the integer value 42.

An expression can appear anywhere in the string, so you can embed a value in a sentence:

>>> camels = 42
>>> f'I have spotted {camels} camels.'
'I have spotted 42 camels.'
Several expressions can be included within a single string literal in order to create more complex strings.

>>> years = 3
>>> count = .1
>>> species = 'camels'
>>> f'In {years} years I have spotted {count} {species}.'
'In 3 years I have spotted 0.1 camels.'
Formatted string literals are powerful, and they can do even more than is covered here. You can read more about them at

https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals.


**Debugging**

A skill that you should cultivate as you program is always asking yourself, “What could go wrong here?” or alternatively, “What crazy thing might our user do to crash our (seemingly) perfect program?”

For example, look at the program which we used to demonstrate the while loop in the chapter on iteration:

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Code: https://www.py4e.com/code3/copytildone2.py
Look what happens when the user enters an empty line of input:

> hello there
hello there
> # don't print this
> print this!
print this!
>
Traceback (most recent call last):
  File "copytildone.py", line 3, in <module>
    if line[0] == '#':
IndexError: string index out of range
The code works fine until it is presented an empty line. Then there is no zero-th character, so we get a traceback. There are two solutions to this to make line three “safe” even if the line is empty.

One possibility is to simply use the startswith method which returns False if the string is empty.

if line.startswith('#'):

Another way is to safely write the if statement using the guardian pattern and make sure the second logical expression is evaluated only where there is at least one character in the string:

if len(line) > 0 and line[0] == '#':