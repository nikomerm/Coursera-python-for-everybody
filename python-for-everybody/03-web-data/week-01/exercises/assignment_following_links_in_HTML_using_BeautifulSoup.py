# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and 
# the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Keayn.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: N

# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program.
# But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program.
# But that is not the point. The point is to write a clever Python program to solve the program.

# What the task asks, in plain words:

# 1.Open a page and collect all its links (a tags).
# 2.Pick the link at position 18 (position 1 is the first link).
# 3.Follow it: open that page and repeat.
# 4.Do this 7 times in total, and the answer is the name on the last page you reach.

# SAMPLE PROBLEM AND EXPLANATION OF THE ASSIGNMENT

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'  #Creates a variable url holding the address of the starting page.

# for i in range(4):                                          #Starts a loop that runs 4 times. range(4) gives the numbers 0, 1, 2, 3, and i takes each one in turn. You never use i inside, it just counts the rounds. Everything indented below belongs to the loop.
#     html = urlopen(url, context=ctx).read()                 #Downloads the page at the current url and stores its raw HTML in html. context=ctx is the SSL setting from the top of your file. In round 1 this is the Fikret page, in round 2 it’s the page you just found, and so on.
#     soup = BeautifulSoup(html, "html.parser")               #Gives the raw HTML to BeautifulSoup, which parses it into an object (soup) you can search.
#     tags = soup('a')                                        #Finds all a (link) tags on the page and puts them in a list called tags.
#     tag = tags[2]                                           #Picks the 3rd link from that list (index 2, because Python counts from 0).
#     url = tag.get('href', None)                             #Takes that link’s href (its address) and overwrites url with it. This is the key line: the next round will open this new page instead of the old one.
#     print(url)

#     What happens over the 4 rounds

# Round	Page opened	Link at position 3 becomes url
# 1	Fikret page	Montgomery’s page
# 2	Montgomery’s page	Mhairade’s page
# 3	Mhairade’s page	Butchi’s page
# 4	Butchi’s page	Anayah’s page


#ACTUAL PROBLEM

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Keayn.html'

for i in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    tag = tags[17]
    url = tag.get('href', None)
    print(url)

