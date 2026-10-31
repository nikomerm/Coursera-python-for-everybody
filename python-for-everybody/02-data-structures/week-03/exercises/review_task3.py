# Task 3: Messages per weekday (dictionaries)
# Count how many From lines were sent on each day of the week (Mon, Tue, and so on). Print the days sorted alphabetically, with their counts, for example Fri 20.
# Reviews: a counting dictionary, sorted() on the keys, printing key and value.
# Hint: the day is one of the words in the split From line.
# Use mbox-short.txt

name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        days = (words[2])
        if days not in counts:
            counts [days] = 1
        else:
            counts [days] = counts [days] + 1

for key in sorted(counts):
    print(key, counts[key]) 
         

        