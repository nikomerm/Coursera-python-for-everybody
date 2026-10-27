# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#Desired Output:cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] = counts[email] + 1

bigemail = None
bigcount = None

for key in counts:
    count = counts[key]
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = key
print(bigemail, bigcount)
   
# What the whole program does

# The first loop builds the dictionary: each email is a key, and its value is how many From lines it appeared in.
# The second loop is the maximum pattern from Task 3, applied to the dictionary’s values: it keeps the biggest count seen so far and the email that goes with it.



