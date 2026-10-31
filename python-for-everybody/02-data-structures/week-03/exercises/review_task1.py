# Task 1: Count replies (strings and files)
# Count the lines that start with Subject: and also contain svn somewhere in the line. Print Replies: N.
# Reviews: opening a file, looping over lines, startswith(), the in keyword on strings, counters.
# Use mbox-short.txt

name = input("Enter file:")
if len(name) < 1:   #In the VS Code Explorer (left panel), right-click review_task1.py and choose Open in Integrated Terminal. 
                    #The terminal opens already inside exercises, so the prompt ends in \exercises>. Type python review_task1.py and press Enter at the file prompt.
    name = "mbox-short.txt"
handle = open(name)

count = 0
for line in handle:
    if line.startswith("Subject: ") and "svn" in line:
        count = count + 1
print("Subjects with svn:", count)

