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

Review day : Claude tasks practice. 