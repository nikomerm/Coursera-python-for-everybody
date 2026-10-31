# Task 2: Unique domains (lists)
# For each From line, take the sender’s address and extract the domain, the part after the @. Collect each domain once in a list, then sort the list and print it.
# Reviews: split() twice (on whitespace, then on "@"), not in, append(), sort().
# Hint: it’s the romeo.txt pattern, applied to domains instead of words.
# Use mbox-short.txt

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst=list()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = (words[1])
        pieces = email.split("@")
        domain = (pieces[1])
        if domain not in lst:
            lst.append(domain)

lst.sort()
print(lst)
            

