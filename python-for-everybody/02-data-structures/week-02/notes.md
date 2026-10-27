# 02-data-structures - Week 2

## Τι έμαθα

## Παράδειγμα κώδικα





                                                                **Monday 19/10/2026**
Chapter Seven : Files
Working with files, marking a shift from temporary in memory data to permanent storage.

**File processing part 1:** To work with a file, Python must first open it using the build in open() function

**Opening a file** : 
open() function , wich returns a file handle - a connection to the file, not the file's content itself.
The file handle allows reading from or writing to the file and must be closed after operations are complete. The purpose of a file handle in Python is to serve as a connection or interface between your program and a file on disk.

**Newline Characters and File Structure**

Newline characters (\n) represent the end of a line in a file and are treated as a single non-printing character in Python strings.
Files are essentially long strings of characters punctuated by these newline characters, which are important for understanding how text files are structured and processed.

**Why it is important:**

It tells the program where one line ends and the next begins, effectively separating lines in a file.
When reading or writing files, recognizing newlines helps process the file line by line.
It ensures the file's text structure is preserved, including blank lines.

**example of opening a file:**

# Open the file named 'mbox.txt' for reading
file_handle = open('mbox.txt')

# Read the file line by line
for line in file_handle:
    # Print each line after stripping the newline character at the end
    print(line.strip())

# Close the file when done
file_handle.close()

**Explanation:**

open('mbox.txt') tells Python to open the file called 'mbox.txt' for reading (this is the default mode).

The file_handle is like a window to the file, not the file content itself.

The for line in file_handle: loop reads the file one line at a time, which is like reading a book page by page.

line.strip() removes the invisible newline character at the end of each line so the print looks neat.

Finally, file_handle.close() closes the window to the file, which is good practice to free up resources.



**File processing part 2:**   reading files line by line and processing their contents efficiently.

**Reading Files Line by Line**

A file handle in Python can be treated as a sequence of lines, allowing iteration with a for loop.
Each iteration variable represents one line from the file, making it easy to process files without manual end-of-file checks.

**example:** When you want to read a file line by line in Python, you can use a for loop directly on the file handle. Think of the file as a book, and each line is a page. The for loop helps you turn the pages one by one, reading each line without needing to know how many lines there are in advance.
# Open the file for reading
fhand = open('example.txt')

# Loop through each line in the file (The for line in fhand: loop reads one line at a time).
for line in fhand:
    # Remove any extra whitespace or newline characters at the end rstrip() to avoid extra blank lines when printing.
    line = line.rstrip()
    # Print the line
    print(line)

# Close the file when done
fhand.close()

**Counting and Reading Entire Files**

You can count lines by looping through the file and incrementing a counter for each line.
The .read() method reads the entire file content as a single string, including newline characters, which requires careful handling.

**Filtering and Processing Lines**

You can filter lines by checking conditions like whether a line starts with a specific string (e.g., "From:") and print or process only those lines.
To avoid extra blank lines when printing, use the rstrip() method to remove trailing whitespace and newlines from each line before printing.

**Handling User Input and Errors**

File names can be read from user input to open different files dynamically.
Using try and except blocks helps handle errors gracefully when a file cannot be opened, preventing program crashes and providing user-friendly error messages.

**Control Flow Techniques**

The continue statement can be used to skip uninteresting lines in a loop, improving code readability and logic flow.
Both positive filtering (if line starts with) and negative filtering (if not line starts with) approaches are demonstrated for selecting lines of interest.

**example:** This example reflects the key ideas from the lecture about file reading, filtering, error handling, and control flow. 

def process_file(filename, keyword):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return

    count = 0
    for line in lines:
        # Filter lines containing the keyword (case-insensitive)
        if keyword.lower() not in line.lower():
            continue  # Skip lines without the keyword
        count += 1
        print(line.rstrip())  # Print filtered lines without extra blank lines

    print(f"\nTotal lines containing '{keyword}': {count}")

def main():
    while True:
        filename = input("Enter the filename to process (or 'exit' to quit): ")
        if filename.lower() == 'exit':
            print("Exiting program.")
            break

        keyword = input("Enter the keyword to filter lines: ")
        if not keyword:
            print("Keyword cannot be empty. Please try again.")
            continue

        process_file(filename, keyword)

if __name__ == "__main__":
    main()

    Summary of what this code does:

Prompts the user to enter a filename and a keyword.
Tries to open and read the file, handling errors gracefully.
Reads all lines and filters them to print only those containing the keyword.
Uses continue to skip lines that don't match the filter.
Counts and prints the number of matching lines.
Allows the user to repeat or exit.


                                                                    **Tuesday 20/10/2026**

Review day : Claude tasks practice in excercises folder week-02.

                                                                    **Wednesday 21/10/2026**
**Chapter 8 Lists**

Data Structures: Algorithms are paths that code follows, while data structures are ways to organize variables and memory.
Lists, dictionaries, and tuples are key data structures that allow storing multiple values in one variable.

Lists are collections enclosed in square brackets, capable of holding multiple items of different types, including other lists.
Lists are mutable, meaning their contents can be changed after creation, unlike strings which are immutable.

# Creating a list with different types of items, including another list
my_list = ["apple", 42, 3.14, ["nested", "list"]]

print("Original list:")
print(my_list)              #my_list contains a string, an integer, a float, and another list.

# Changing the second item (index 1) from 42 to 100
my_list[1] = 100

print("\nList after changing the second item:")
print(my_list)                       #We change the integer 42 to 100 by assigning a new value to my_list[1].

# Trying to change a character in a string (this will cause an error)
fruit = "banana"
# fruit[0] = "B"  # This line would cause an error because strings are immutable

# Instead, we create a new string
new_fruit = "B" + fruit[1:]
print("\nOriginal string:", fruit)
print("New string after change:", new_fruit)   #Strings cannot be changed character by character, so to "change" a string, we create a new one. 
 #Original string: banana
 #New string after change: Banana

 **List Operations and Slicing**

Lists can be concatenated using the + operator, similar to strings, without altering the original lists.

Slicing works like with strings, allowing extraction of sublists by specifying start and end indices, with the end index being exclusive.

# Define a list of numbers
numbers = [10, 20, 30, 40, 50, 60]

# Slice from index 1 up to but not including index 4
slice_1 = numbers[1:4]  # [20, 30, 40]

# Slice from start up to but not including index 3
slice_2 = numbers[:3]   # [10, 20, 30]

# Slice from index 3 to the end
slice_3 = numbers[3:]   # [40, 50, 60]

**List Methods and Mutability**

Lists have various methods such as append (adds an item to the end), count, extend, index, insert, pop, and remove.

Unlike strings, lists are mutable, so methods like append modify the list in place without returning a new list.

**Using Lists in Loops and Functions**

The 'in' and 'not in' operators check for membership within a list.

Lists maintain the order of elements, and methods like sort can reorder the list in place.

Functions like len, max, min, and sum help analyze list contents.

Examples show how to calculate averages using loops and lists, illustrating memory considerations between accumulating sums directly versus storing values in a list first.



# Create an empty list
stuff = list()

# Append items to the list
stuff.append("book")
stuff.append(99)
stuff.append("cookie")

print("Initial list:", stuff)

# Slice the list: get items from index 1 up to but not including 3
slice_example = stuff[1:3]
print("Sliced list (index 1 to 2):", slice_example)

# Check if an item is in the list
print("Is 99 in the list?", 99 in stuff)
print("Is 15 in the list?", 15 in stuff)

# Sort a list of strings
friends = ["Joseph", "Glenn", "Sally"]
print("Friends before sort:", friends)
friends.sort()
print("Friends after sort:", friends)

# Calculate sum and average of a list of numbers
numbers = [3, 9, 5]
total = sum(numbers)
count = len(numbers)
average = total / count
print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


# Imagine you have a list of numbers, and you want to find out how many of those numbers are greater than 10. Here's how you could do it with a loop:

numbers = [4, 11, 15, 7, 20, 3]
count_greater_than_10 = 0

for num in numbers:
    if num > 10:
        count_greater_than_10 += 1

print("Numbers greater than 10:", count_greater_than_10)   #This is like counting how many apples in a basket are bigger than a certain size by looking at each apple one by one.


# List & Strings working together

# !!!! Pattern for how we read a line , break it into pieces and then look each word in the line .split() and then a for loop. !!!!

. If you want to break a string into words, you can use the split method:


>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']
>>> print(t[2])
the


Once you have used split to break the string into a list of words, you can use the index operator (square bracket) to look at a particular word in the list.

You can call split with an optional argument called a delimiter that specifies which characters to use as word boundaries. The following example uses a hyphen as a delimiter:


>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']

# another example with split()

**Example 1: split, then loop over the words**
line = "But soft what light"
words = line.split()

for word in words:
    print(word)

**Output:** 
But
soft
what
light    #split() makes the list, and the for loop visits one word at a time.


**Example 2: count the words in a line**
line = "It is the east and Juliet is the sun"
count = 0

for word in line.split():
    count = count + 1

print(count)   

**Output:** 9           ## You can write line.split() directly in the for line, so you don’t need a separate words variable.


**Example 3: split on a different character**

email = "stephen.marquard@uct.ac.za"
parts = email.split("@")

for part in parts:
    print(part)

**Output:**                  #With an argument, split() cuts at that exact text instead of at spaces.
stephen.marquard
uct.ac.za

**Example 4: loop over a file, then over each line’s words**

fh = open("romeo.txt")

for line in fh:
    words = line.split()
    print("Words on this line:", len(words))
    for word in words:
        print("   ", word)   
        
**Output:** This is the nested pattern from your assignment: the outer loop goes through lines, and the inner loop goes through the words of the current line. len(words) gives the number of items in a list.

**Example 5: Here’s one example that combines all four pieces. It finds the words in a sentence that start with a given letter**

line = "But soft what light through yonder window breaks"
count = 0

for word in line.split():
    if word.startswith("w"):
        print(word)
        count = count + 1

print("Words starting with w:", count)

**Output:**
what
window
Words starting with w: 2           

#How it works

line.split() makes the list of words.
for word in ... visits one word at a time.
word.startswith("w") is true only if that word begins with w. Here it’s called on a word, not a whole line.
The if decides which words get printed and counted.


# The guardian pattern in Python is a programming practice where you add a condition to check for potential problems before executing code that might cause errors. It acts as a "guard" to prevent the program from crashing by skipping or handling problematic cases early.

Why it is important:

It prevents runtime errors like "index out of range" by ensuring the data meets certain conditions before accessing it.
It makes the code more robust and reliable when dealing with unpredictable or messy data.
It helps maintain program flow by safely handling edge cases, such as blank lines or missing data.
#Understanding the Guardian Pattern with a Simple Example

The guardian pattern is like having a safety guard in your code that checks if everything is okay before moving forward. Imagine you're about to open a box, but first, you check if the box is actually there and not empty. If the box is empty, you skip opening it to avoid problems. In programming, this means checking if the data you want to use is valid before using it, so your program doesn't crash.

Here's a simple example in Python that shows this idea. Suppose you have a list of words from a sentence, and you want to print the first word only if the list is not empty:

words = input("Enter a sentence: ").split()

 #Guardian pattern: check if the list has at least one word
if len(words) < 1:
    print("No words to process, skipping.")
else:
    print("The first word is:", words[0])
In this example, the guardian pattern is the if len(words) < 1 check. It protects the program from trying to access the first word when there are no words, which would cause an error. This way, the program safely handles empty input.



                                                                **Friday 23/10/2026**
**Data Structures : Dictionaries : Chapter 9**

What are dictionaries? : 
Dictionaries in Python are like special collections that store information in pairs, where each piece of information has a unique label or "key."
dictionaries use these keys to find values directly. This makes dictionaries very powerful and popular because you can store and access data quickly using meaningful tags instead of just numbers. In Python, you create a dictionary using curly braces {} and add items by assigning a value to a key, like this:

cabinet = {}
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet['fall'])  # This will print 3
Here, 'summer', 'fall', and 'spring' are keys, and 12, 3, and 75 are their corresponding values.


**Comparing Dictionaries Vs Lists:**
Lists, are like a row of numbered boxes where you can only find things by their position, like the first box, second box, and so on. If you want the third item, you say list[2] (because counting starts at zero). Lists are great when order matters or when you want to go through items one by one. 
But if you want to find something quickly by a name or label, dictionaries are much better because they let you jump straight to the item without searching through everything.

**Key Differences Between Lists and Dictionaries in Python:**

**Indexing:**
Lists use integer indices starting at 0 to access elements by position.
Dictionaries use keys (often strings) to access values by label.

**Order:**
Lists maintain the order of items as inserted.
Dictionaries (since Python 3.7) maintain insertion order but are accessed by keys, not position.

**Use Case:**
Lists are ideal for ordered collections where position matters.
Dictionaries are ideal for collections where you want to look up values by meaningful keys quickly.

**Syntax:**
Lists use square brackets: [value1, value2, value3]
Dictionaries use curly braces with key-value pairs: {'key1': value1, 'key2': value2}
In short, use lists when order and position matter, and use dictionaries when you want to associate values with unique keys for fast lookup.


# Part 2 Dictionaries: Counting with Dictionaries

How Python uses dictionaries to create histograms, which count occurrences of items such as names.
A **histogram** is a graphical bar chart that shows the frequency distribution of continuous numerical data. (Ένα ιστόγραμμα είναι μια γραφική απεικόνιση δεδομένων που δείχνει πώς κατανέμονται οι τιμές σε ένα σύνολο πληροφοριών, χρησιμοποιώντας παρακείμενα ορθογώνια (στήλες))
**Histogram Concept**
A histogram counts how many times each item appears, storing the counts in a dictionary with items as keys and counts as values.
This approach scales to large datasets, allowing counting of millions of items efficiently.

**Handling Dictionary Keys**

Directly accessing a dictionary key that doesn't exist causes an error **(traceback)**, but this can be avoided by checking if the key is in the dictionary using the "in" operator.
Using an if-else structure, you can initialize the count for a new key to 1 or increment the count if the key already exists.

**Example:**

names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
counts = {}

for name in names:
    if name not in counts:
        counts[name] = 1  # First time seeing the name, start count at 1
    else:
        counts[name] = counts[name] + 1  # Name already in dictionary, add 1 to count

print(counts)

**Explanation:**

We start with an empty dictionary counts.
For each name in the list, we check if it's already a key in counts.
If not, we add it with a count of 1.
If it is, we increase the existing count by 1.
At the end, counts holds the total number of times each name appeared.
This approach helps you safely add or update dictionary entries without causing errors.

**Using the get() Method**

The dictionary method get() simplifies counting by returning the current count or a default value (like 0) if the key is not present.
This reduces multiple lines of code into a single line, making the code cleaner and less error-prone.

**Example:**

names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
counts = {}

for name in names:
    counts[name] = counts.get(name, 0) + 1  # Get current count or 0 if not present, then add 1

print(counts)

**Explanation:**

counts.get(name, 0) returns the current count for name if it exists; otherwise, it returns 0.
We add 1 to that value and store it back in the dictionary.
This replaces the if-else check with a single line, making the code cleaner and easier to read.


**How do you loop through keys and values in a Python dictionary?**

To loop through keys and values in a Python dictionary, you use the .items() method, which returns key-value pairs as tuples. You can unpack these tuples directly in the for loop.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(key, value)
This will print each key and its corresponding value. Using .items() is the most common and efficient way to access both keys and values during iteration.



**Practical example using get() method**

To count words in a text file using a dictionary, you can follow these steps:

1.Open the file for reading.
2.Read the file line by line.
3.Split each line into words.
4.For each word, update the count in the dictionary using the get() method.

counts = {}

with open('filename.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

print(counts)

**Explanation:**

Replace 'filename.txt' with your actual file name.
The split() method breaks each line into words based on whitespace.
The dictionary counts keeps track of how many times each word appears.