#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
#Desired Output: Average spam confidence: 0.7507185185185187

total = 0
count = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    colon_index = line.find(":")
    value_str = line[colon_index + 1:]
    count = count + 1
    total = total + float(value_str)

av_sp_con = total / count
print("Average spam confidence:", av_sp_con)


