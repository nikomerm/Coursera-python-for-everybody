#Task 2: Filter and clean
#Print only the lines that start with Subject:, in lower case, with no blank lines between them. After the loop, print how many you found.
#Reviews: startswith(), rstrip(), lower-casing a string, continue or if.


count=0
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if line.startswith("Subject:"):
        line=line.strip()
        print(line.lower())
        count = count + 1

print("Subject count: ",count)
