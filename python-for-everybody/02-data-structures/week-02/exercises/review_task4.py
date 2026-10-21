# Task 4: Sender list with error handling
# Prompt for a file name. If the file can’t be opened, print File cannot be opened: followed by the name, and quit. 
# Otherwise, for each line starting with From (note the space, not a colon), extract the email address and print it.
# At the end, print There were N lines in the file with From as the first word.
# Reviews: try/except, split(), indexing a list of words, quit().
# Hint: a line like From stephen.marquard@uct.ac.za Sat Jan 5 ... splits into words, and the address is one of them.

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")


# #explanation line by line

# try:: tells Python “attempt the indented code below, and if it causes an error, don’t crash, jump to except instead.”

# fh = open(fname): tries to open the file. If the file exists, fh becomes the file handle and Python skips the except block. If not, Python raises an error right here.

# except:: the code under this runs only when something in the try block failed. It must line up with try.

# print("File cannot be opened:", fname): shows the message plus the name the user typed, so they can see what went wrong.

# quit(): stops the whole program. Without it, the code below would run with no fh and crash anyway.

# count = 0: a counter for the From lines, set before the loop so it starts fresh and isn’t reset on each pass.

# for line in fh:: goes through the file one line at a time, putting each line in line.

# if not line.startswith("From "):: true when the line does not begin with From (with a space).
# The space matters: it excludes lines like From: someone@..., which are a different header.

# continue: for non-matching lines, skip the rest of the loop body and move to the next line. Only From lines continue past this point.

# words = line.split(): breaks the line into a list of words, splitting on whitespace. 
# A line like From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 becomes:['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
# Because split() handles the trailing newline as whitespace, you don’t need rstrip() here.

# print(words[1]): lists are numbered from 0, so words[0] is From and words[1] is the email address. This prints just the address.

# count = count + 1: adds 1 for each matching line.

# print("There were", count, "lines in the file with From as the first word"): not indented, so it runs once after the loop ends. 

