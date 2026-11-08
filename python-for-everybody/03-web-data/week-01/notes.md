# 03-web-data - Week 1

## Τι έμαθα

## Παράδειγμα κώδικα

                                                            **Saturday 31/10/2026**
# Using Python to Access Web Data
# Chapter Eleven: Regular Expressions


**What are Regular Expressions:**
Regular expressions, often called "regex," are like a secret code or a special pattern language that helps you find and work with text in a smart way.
Imagine you have a huge book and you want to find all the sentences that start with the word "Hello" or all the email addresses hidden inside. Instead of reading every line carefully, you can use regular expressions to quickly spot these patterns. It's like having a super-powered search tool that understands patterns, not just exact words.
Regular expressions (regex) are a way to describe a pattern of text, so Python can find or extract it from a bigger piece of text.
Think of it as a “smart search.” Normal search finds exact words. Regex finds shapes:

“any number”
“an email address”
“a word that starts with a capital letter”

Example:

import re

text = "My phone is 6912345678 and my code is 42"
re.findall('[0-9]+', text)
   #['6912345678', '42']                    #[0-9]+ means “one or more digits in a row.”

In Python, regular expressions are used through a special library called "re." You first import this library, then you can use functions like re.search() to check if a pattern exists in a string, or re.findall() to pull out all parts of the text that match your pattern.

For example, the pattern "^X.*:" means "a line that starts with 'X', followed by any number of characters, and then a colon." This can match lines like "X-Something:" but not lines that don't follow this pattern.
Using regular expressions can save you from writing lots of complicated code to search and extract text. They might look cryptic at first, but once you get the hang of the symbols and how to combine them, they become a powerful tool in your programming toolkit.

A few basic symbols:

 Symbol	               Meaning

 .	                   any one character
 \d or [0-9]	           a digit
 \S	                   any non-space character
 +	                   one or more of the previous
 *	                   zero or more of the previous
 ^	                   start of the line
 $	                   end of the line
 ( )	                   extract only this part

In a nutshell: regex = a mini-language for describing text patterns, used with re.search() (does it match?) and re.findall() (give me all matches). 

#      EXTRACTING DATA 
Fine-tuning extraction = using parentheses ( ) to tell regex: “match the whole pattern, but give me back only this part.”

Without parentheses you get the whole match:
import re

line = "From: stephen@umich.edu Sat Jan 5"
re.findall('\S+@\S+', line)
                                    # [In a nutshell: find + slicing = manual way (3 lines), regex = same result in 1 line. 'stephen@umich.edu']

                                    Here it matched an email, and returned all of it. Fine.

With parentheses you can match a bigger pattern but extract only a piece:
re.findall('^From (\S+@\S+)', line)

Careful: my line above has From: with a colon, so this wouldn’t match. With the real mail format From stephen@umich.edu Sat Jan 5, it would return:
['stephen@umich.edu']

How it works:

^From → the line must start with “From “ (this is used to find the right line, but it’s not returned)
(\S+@\S+) → only this part is returned

**Another example: extract just the domain**

line = "From stephen@umich.edu Sat Jan 5"
re.findall('@(\S+)', line)
                            # ['umich.edu']
@ is used for matching, but only what’s inside ( ) comes back.

In a nutshell: the whole pattern decides what matches, the parentheses decide what you get back.

# Classic example from the course: get the host (domain) from a “From” line, without regex, using find() and slicing.

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

at = line.find('@')              # position of the @
space = line.find(' ', at)       # first space AFTER the @
host = line[at+1 : space]        # slice between them

print(host)
    # uct.ac.za

    How it works:

line.find('@') → index of @ (here 21)
line.find(' ', at) → looks for a space starting from position at, so it finds the one right after the email
line[at+1 : space] → starts one character after @ (so @ is not included) and stops before the space

# The “double split” pattern from the course: split the line into words, then split the email on @.
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

words = line.split()          # split on spaces
email = words[1]              # 'stephen.marquard@uct.ac.za'

pieces = email.split('@')     # split the email on @
host = pieces[1]              # 'uct.ac.za'

print(host)
    # uct.ac.za

    How it works:

line.split() → ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', ...]
words[1] → the second word, the email
email.split('@') → ['stephen.marquard', 'uct.ac.za']
pieces[1] → the part after the @

# Same thing with regex, for comparison:

import re
re.findall('@(\S+)', line)
    # ['uct.ac.za']

In a nutshell: find + slicing = manual way (3 lines), regex = same result in 1 line.


# Example of extracting all the words that start from letter a from a file 

import re

handle = open("myfile.txt")
words = []

for line in handle:
    found = re.findall('\\ba[a-z]*', line, re.IGNORECASE)
    for w in found:
        words.append(w)

print(words)

\ba[a-z]* = “a word that starts with a”.
re.IGNORECASE tells regex: “don’t care about capital vs lowercase.”
case-sensitive: a and A are different characters. So \ba[a-z]* only finds words starting with a small a.
With the flag, a matches both a and A, and [a-z] matches capitals too.


                                                                **Sunday 01/11/2026**
# Chapter 12 Networks and Sockets
# Networked Technology 
**Network Data part 1**
TCP (Transmission Control Protocol) is a core protocol of the transport layer in the Internet architecture.Handles flow control.
~Reliable Communication: TCP provides a reliable, ordered, and error-checked delivery of a stream of data between applications running on hosts communicating via an IP network
~Connection-Oriented: Before data is sent, TCP establishes a connection (a socket) between the two endpoints, like making a phone call.
~Data Stream: TCP treats data as a continuous stream of bytes, ensuring that data sent from one end is received in the same order on the other end.
~Ports: TCP uses ports to differentiate between multiple applications on the same server (e.g., port 80 for HTTP).
~Socket: A TCP socket is the endpoint for sending or receiving data, created in Python using the socket library.

The **end-to-end layer** is where your Python program talks directly to another application on a remote server, managing the connection and data transfer.
When you write Python programs that communicate over the Internet using sockets, you are working at this transport (end-to-end) layer.Its main job is to provide reliable communication between two applications running on different computers (endpoints).It establishes a connection (like a phone call) between the two applications, ensuring data is sent and received correctly.
This layer handles data segmentation, error checking, and flow control.
TCP (Transmission Control Protocol) is the most common protocol used at this layer, providing reliable, ordered data delivery

A **network socket** is one endpoint of a two-way communication link between two programs over a network. It’s defined by an IP address plus a port number (e.g. 192.168.1.5:8080), and programs use it to send and receive data, usually over TCP (reliable, connection-based) or UDP (fast, connectionless).
Think of it like a phone: the IP is the phone number, the port is the extension, and the socket is the handset you talk through - the phone call.

# In a nutshell, using TCP:

Server side

Create a socket
Bind it to an IP and port (its “address”)
Listen for incoming connections
Accept a client, which gives a new socket just for that conversation

Client side

Create a socket
Connect to the server’s IP and port

Then both sides

Send / receive data through the socket
Close it when done

**What is a TCP port**: A TCP port is a number (0-65535) that identifies a specific program or service on a computer, so incoming data reaches the right one. Extensions of the phone.

An IP address gets data to the right machine; the port gets it to the right application on that machine. Your computer might run a web server, an email client, and a game all at once, and each listens on a different port.Ports act like extension numbers that organize and route network traffic to the right programs on a computer.

Imagine an apartment building.

The building’s street address is the IP address. It gets the mail to the right building.
The apartment number is the port. It gets the mail to the right person inside.

**Sockets in Python**

In Python, you use the built-in socket module. The workflow is always the same pattern:

Server

1. socket.socket() creates the socket
2. .bind((ip, port)) attaches it to an address
3. .listen() waits for clients
4. .accept() accepts one and returns a new socket (conn) plus the client’s address (addr)
5. .recv(size) / .send(data) exchange data
6. .close() ends it

Client

1. socket.socket() creates the socket
2. .connect((ip, port)) reaches the server
3. .send(data) / .recv(size) exchange data
4. .close() ends it

Two things to remember:

Data is sent as bytes, not strings. Use .encode() before sending and .decode() after receiving.
socket.socket() defaults to IPv4 + TCP, which is what you want here.

**Server (run this first)**

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen()
print("Waiting for a client...")

conn, addr = server.accept()
print("Connected by", addr)

data = conn.recv(1024).decode()
print("Client says:", data)

conn.send("Hello from server!".encode())

conn.close()
server.close()

**Client (run this second, in another terminal)**

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

client.send("Hello from client!".encode())

reply = client.recv(1024).decode()
print("Server says:", reply)

client.close()


AF_INET means IPv4 and SOCK_STREAM means TCP.
Expected output:

Server terminal: Client says: Hello from client!
Client terminal: Server says: Hello from server!



                                                                **Monday 02/11/2026**


# Network Programs Part 2

**HTTP** Hypertext Transfer Protocol
Is the dominant Aplication Layer Protocol on the internet.It was invented to retrieve web pages. HTTP is the set of rules to allow browsers to retrieve web documents from servers over the internet.

protocol     host         document
http://www.dr-chuck.com/page1.htm

Http:// : says use the HTTP protocol
www.dr-chuck.com : says go to this host
/page1.htm: says go get this document

What is a HTTP request in Python:

~make a connection to a port           <------Shows how you open
~send a get request                    <------a socket, send a command
~get some data back                    <------and then retrieve the data

code example:

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0/r/n/r/n'.encode()
mysock.send(cmd)

While True:
    data = mysock.recv(512)
    if (len(data) <1 ) :
        break
    print(data.decode())
mysock.close()       


# Network Programs Part 3

Chapter 12: Unicode Characters and Strings

Computers only store numbers (binary), so every character gets assigned a number, and that number is what’s actually stored.So computers represent text characters using numeric codes.
            **ASCII (the early standard)**
Each character maps to a number from 0 to 127
Examples: A = 65, B = 66, a = 97, 0 = 48, space = 32
Fits in 7 bits, stored in 1 byte
Covers only English letters, digits, and basic symbols

Unicode (the modern solution)
Gives every character in every language its own number, called a code point. In python 3, all strings are Unicode

          UTF-8 (how Unicode is stored)
Stores each code point in 1 to 4 bytes
It’s the most common encoding on the web. Is recommended practise for encoding data to be exchanged between systems, due to its efficiency and compatibility. Its the default and most common encoding. 

Before we send data and beforfe receive , we have to encode and decode this stuff, so that it works out correctly.

                                                        **Wednesday 04/11/2026**

# Network Programs Part 4                                  

**Retrieving Web Pages**

Retrieving web pages means the process where a client (such as a web browser, script, or crawler) requests and downloads content from a web server on the Internet.
We do that by using urllib, since HTTP is so common we a library that does all the socket work for us and makes web pages look like a file.
Urllib abstracts socket and HTTP communication, making it easier to open URLs and read Web Content.
The data read from a URL comes as bytes, so decoding to a string is necessary.

# Network Programs Part 5

**Parsing Web Pages**

Parsing meaning: is the process of breaking down a sequence of symbols, text, or data into smaller, individual components and analyzing how they relate to one another according to a set of grammatical or structural rules. In Computer Science and Programming : Converting raw, unstructured text or data into a structured format (such as a parse tree or Abstract Syntax Tree) that a computer program can easily read, evaluate, or execute. (μεταφράζεται στα ελληνικά κυρίως ως συντακτική ανάλυση ή ανάλυση)

Web Scraping meaning: is the automated process of extracting raw data from websites and converting it into structured formats like CSV, JSON, or databases.
Aυτόματη συλλογή δεδομένων ή εξαγωγή δεδομένων από ιστοσελίδες (η αυτόματη «αντιγραφή» ή «συλλογή» πληροφοριών, όπως τιμές προϊόντων, κείμενα ή επαφές, από ένα site σε μορφή Excel/database).
Pull Data , Get your own data back out of a system that has no export capability, Monitor a site for information, Spider the web to make a database for a search engine.

**Why the bigest problem in spidering is the parsing of the HTML that comes back?**
(Web Spidering : also known as web crawling or web indexing) is the automated process in which an internet bot (called a spider or crawler) systematically browses the World Wide Web to discover, read, and catalog web pages.

Answer: Browsers and HTML are forgiving. If a tag is unclosed or badly nested, the browser quietly guesses what the author meant and displays the page anyway. HTML has no “syntax error” crash like Python does. So websites get away with sloppy code, and a lot of real-world HTML is broken in small ways. That’s what makes parsing hard. When your program reads the HTML, it has to pull out specific pieces (like links). If you write simple code that expects clean, predictable structure, it breaks on:
Missing or unclosed tags (<p> with no </p>)
Wrong nesting (<b><i>text</b></i>)
Odd attributes, inconsistent quotes, extra spaces
Every site being structured differently

The solution: BeautifulSoup

#                                                                Summary of Network Programs

**The TCP/IP gives us pipes/sockets between applications** : TCP/IP lets two programs on different computers connect and exchange data, like a pipe between them. The socket is each end of that pipe.

**We designed application Protocols to make use of these pipes** : Application protocols (like HTTP) are the agreed rules for what programs say to each other through those pipes, so both sides understand the messages.

**HyperText Transfer Protocol (HTTP) is a simple yet powerful protocol** : HTTP is simple because it works like a basic conversation: the client sends a request (“give me this page”), and the server sends back a response (the page). Powerful because that one pattern runs the whole web.

**Python has good support for sockets , HTTP and HTML parsing** : Python comes with built-in tools for each layer: the socket module for connections, urllib for HTTP requests, and libraries like BeautifulSoup for reading HTML, so you rarely have to build it all from scratch.


## 1 TCP/IP gives us pipes/sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))        # the pipe is open

#  2 Application protocol (HTTP) = the rules for talking through the pipe
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)                             # 3 the REQUEST

#  3 ...and the RESPONSE comes back
data = mysock.recv(512)
print(data.decode())                         # headers + page
mysock.close()

#  4a Python's HTTP support: urllib does all of the above in 1 line
import urllib.request
html = urllib.request.urlopen('http://data.pr4e.org/page1.htm').read()

#  4b Python's HTML parsing: BeautifulSoup reads the messy HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for tag in soup('a'):                        # find all links
    print(tag.get('href'))

**The flow: socket (pipe) → HTTP (rules) → request/response → urllib (easy HTTP) → BeautifulSoup (read the HTML).**


                                                        **Friday 06/11/2026**


# Chapter 13: Web Services Part 1

Web services describe how data is exchanged between programs over the internet using agreed-upon formats
Web services formalize the process of moving data between programs using the HTTP request/response cycle.
Programs communicate by sending data structures (e.g., Python dictionaries) across networks in a language-neutral format.
While data is being exchanged between programs using protocols with the HTTP Request/Response cycle, there is a need of a way to represent these data with a specific format: XML & JSON

**What is the network?**

Simple: two or more computers connected so they can exchange data.
Physical: the cables, Wi-Fi, routers, and switches that carry bytes between machines.
Layered (more technical): the stack of protocols (Ethernet, IP, TCP, then HTTP on top) that gets bytes from A to B.

The network is the medium (μέσο) that carries bytes. The wire protocol is the agreement on how data is formatted as bytes (JSON, XML, Protocol Buffers).


#                       Python Dictionary => serialize (JSON/XML) => bytes over Network => deserialize => Java HashMap


Python serializes it into bytes in an agreed format, the bytes cross the network, and Java deserializes them into a HashMap.
- Network: the medium that carries the bytes
- Wire protocol: the agreed format of those bytes


**Serialization** = converting an in-memory object into a sequence of bytes (or text) that can be sent or stored.
**Deserialization** = the reverse: rebuilding the object from those bytes.
- Serialization: object in memory -> bytes/text (JSON, XML) to send or store
- Deserialization: bytes/text -> object in memory on the receiving side
- Needed because different systems (Python, Java) store data differently, so they share a common format

JSON mostly replaced XML for web APIs because it’s lighter and easier to read. XML is still used in older enterprise systems, SOAP services, and config files.
Libraries do it for you: json.dumps() / json.loads() in Python.You rarely write it by hand, but you need to understand it to debug problems like “why is this field missing?” or “why did my date become a string?”

# XML (eXtensible Markup Language)

What XML is:
A text format for structured data using nested tags.
Self-describing: tags name the data.

<user id="1">
  <name>Nikos</name>
  <age>30</age>
</user>

Core rules (well-formed XML)

Exactly one root element.
Every opening tag needs a closing tag (or <tag/>).
Tags are case-sensitive and must nest properly.
Attribute values go in quotes (id="1").

**Concepts worth knowing**

Elements vs attributes: <user id="1">, where id is an attribute and <name> is a child element.
XSD (schema): defines what a valid document looks like (types, required fields). This is XML’s big strength over plain JSON.
Namespaces: prevent tag name clashes (xmlns). You’ll see them in SOAP(Simple Object Access Protocol).
XPath: a query language for finding nodes, e.g. /user/name.
XSLT: transforms XML into other formats. Rarely needed.

Where you’ll still meet it:

SOAP(Simple Object Access Protocol) web services: banks, insurance, government, and older enterprise systems. #SOAP request:SOAP (Simple Object Access Protocol) is an older web service standard. You send an XML message, called an envelope, over HTTP (usually POST) to a server, and you get an XML message back.
Config files: Maven pom.xml, Android layouts, Spring configs.
Document formats: .docx and .xlsx are zipped XML.
RSS/Atom feeds and SVG.

As a backend dev, you should be able to:

Read and write simple XML by hand.
Parse it in code (Python: xml.etree.ElementTree).
Explain XML vs JSON and when XML still makes sense.
Recognize a SOAP request and know it’s XML over HTTP.

## XML
- Tag-based, self-describing text format; one root, tags must close and nest properly
- XSD = schema validation, XPath = query nodes, namespaces = avoid tag clashes
- Still used in: SOAP, config files (pom.xml), .docx/.xlsx, RSS
- JSON replaced it for most web APIs (lighter), XML stays in legacy/enterprise
- Python parsing: xml.etree.ElementTree


**XML Schema and Validation**:

XML Schema defines the structure and data types of XML documents to ensure data correctness and agreement between applications.
Validation is the process of checking an XML document against its schema to confirm it meets the agreed format, independent of data transfer or deserialization.

**Parcing in XML**:
parsing XML means reading XML text and turning it into a structure your code can navigate (deserialization for XML).


# JavaScript Object Notation (JSON)
**Chapter 13: Web Services Part part 5**

 JavaScript Object Notation(συμβολισμός, μορφή)
 Serialization Format: JSON
 JSON is very native to JavaScript & is very simple to use. According to Douglas Crockford(founder): One of the best advantages using JSON is that the data structures thas JSON likes to represent are exactly the same data structures that programming languages represent.

 **Service Oriented Approach - Architecture (SOA)**:

 Allows an application to be broken into parts and distributed across a network.
 SOA is an architecture where an application is split into independent services. Each service does one business job and exposes it through a well-defined interface, and other programs call it over the network, no matter what language or platform they use.

 **Using API (Application Programming Interfaces)**
 An API is a contract for interaction. An API (Application Programming Interface) is a defined interface that lets software components communicate. It specifies what requests you can make, how to make them, and what response you get back.

 # example:
You (the client) sit at the table.
The menu is the API: it lists what you can order.
The waiter carries your request to the kitchen and brings back the food.
You don’t need to know how the kitchen cooks. You only need to know the menu.

**How it connects to what you’ve learned**

A web API is how services in SOA talk to each other.
The request and response are serialized (JSON or XML) and sent over HTTP.
SOAP(XML) and REST(JSON) are two styles of web API.