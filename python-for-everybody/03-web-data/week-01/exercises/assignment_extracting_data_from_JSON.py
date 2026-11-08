# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below:

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2482457.json (Sum ends with 0)

# Data Format:

# The data consists of a number of names and comment counts in JSON as follows:
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }

# The closest sample code that shows how to parse JSON and extract a list is json2.py.
# You might also want to look at xml3.py to see how to prompt for a URL and retrieve data from a URL.


import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2482457.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
info = json.loads(data)
comments = info["comments"]
print(type(comments), len(comments))
print(comments[0])

lst = list()

for values in comments:
    lst.append(values['count'])

print(len(lst))
print(sum(lst))
    


