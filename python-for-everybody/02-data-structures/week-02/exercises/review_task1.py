#Task 1: Line counter
#Prompt for a file name, read through the file, and print Line count: N, where N is the total number of lines.
#Reviews: opening a file, looping over lines, counters.



count=0

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    count = count + 1

print("Line count: ",count)