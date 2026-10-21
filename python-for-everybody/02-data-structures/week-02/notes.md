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