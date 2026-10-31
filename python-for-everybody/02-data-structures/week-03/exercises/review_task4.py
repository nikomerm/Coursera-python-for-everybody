# Task 4: Top 3 domains (dictionaries and tuples)
# Count the messages per sender domain. Then print the 3 domains with the highest counts, highest first, as count domain.
# Reviews: a counting dictionary, .items(), tuples, sorting with reverse=True, slicing a list.
# Hint: build a list of (count, domain) tuples from the dictionary, so that sorting orders by count first.
# Use mbox-short.txt
# Expected output:
# 8 iupui.edu
# 7 umich.edu
# 6 uct.ac.za

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
            words = line.split()
            email = (words[1])
            pieces = email.split("@")
            domain = (pieces[1])
            if domain not in counts:
                counts [domain] = 1
            else:
                counts [domain] = counts [domain] + 1

newlist = list()
for k,v in counts.items() :
     tup = (v,k)
     newlist.append(tup)

cool = sorted(newlist, reverse=True)

for v,k in cool[:3]:
     print(v,k)
            



      


