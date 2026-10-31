# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_2482452.txt (There are 56 values and the sum ends with 388)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and 
# then converting the extracted strings to integers and summing up the integers.

name = input("Enter file:")
handle = open(name)

import re
total= 0

for line in handle:
    line = line.strip()
    y = re.findall('[0-9]+', line)
    for n in y:
        n = int(n)
        total= total + n
print(total)    
    
    
