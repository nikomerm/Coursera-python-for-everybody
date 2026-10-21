
# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)


# Line by line

# lst = list(): the master list, starts empty. It must be created before the loop so it isn’t reset on each line.
# for line in fh:: goes through the file one line at a time.
# words = line.split(): splits the current line into a list of words. It uses a different variable from lst, so the master list isn’t overwritten (your original bug).
# for word in words:: inner loop, handles one word of the current line at a time.
# if word not in lst:: true only if the word hasn’t been collected yet. This is what keeps duplicates out.
# lst.append(word): adds the word to the end of the master list.
# lst.sort(): not indented, so it runs once after all lines are read. It sorts in place, which is why there’s no lst = lst.sort().
# print(lst): prints the final list once. Expected: 26 words, from 'Arise' to 'yonder'.