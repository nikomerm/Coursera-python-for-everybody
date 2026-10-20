# Task 3: Min and max
# Look at the X-DSPAM-Confidence: lines again. Find the smallest and largest values and print both (Smallest: ..., Largest: ...). Don’t use the built-in min() or max().
# Reviews: find() and slicing, float(), comparing values inside a loop.
# Hint: think about how to handle the first value, since you have nothing to compare it to yet.


smallest = None
largest = None

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon_index = line.find(":")
    value_str = line[colon_index + 1:]
    value = float(value_str)

    if smallest is None or value < smallest:
        smallest = value
    if largest is None or value > largest:
        largest = value

print("Smallest:", smallest)
print("Largest:", largest)



#Line by line explanation

# smallest = None and largest = None: None means “no value yet”.
# You can’t start at 0, because 0 would be smaller than every real value and smallest would never update. I renamed your svalue/lvalue to clearer names.

# fname = input("Enter file name: "): asks the user for the file name and stores the text.

# fh = open(fname): opens that file and gives you a file handle you can loop over.

# for line in fh:: runs the indented block once for each line in the file.

# if not line.startswith("X-DSPAM-Confidence:"):: checks whether the line does not begin with that text.

# continue: if the line doesn’t match, skip the rest of the loop body and jump to the next line. Only matching lines go past this point.

# colon_index = line.find(":"): finds the position of the first colon in the line and stores it.

# value_str = line[colon_index + 1:]: slices from one character after the colon to the end of the line. The result is still text, like " 0.8475\n".

# value = float(value_str): converts the text to a real number. float() ignores the leading space and the newline. 
# This is the line you kept getting wrong: you must convert value_str, not line.

# if smallest is None or value < smallest:: true on the first value (nothing to compare yet) or whenever the new value is smaller than the current smallest.

# smallest = value: stores the new smallest.

# if largest is None or value > largest: and largest = value: the same logic in the other direction. 

# These are two separate if statements, not elif, because the first value must set both variables.

# print("Smallest:", smallest) and print("Largest:", largest): not indented, so they run once after the loop finishes. 
