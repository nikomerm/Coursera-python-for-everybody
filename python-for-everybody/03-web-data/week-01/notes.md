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
Think of it like a phone: the IP is the phone number, the port is the extension, and the socket is the handset you talk through.

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

**What is a TCP port**: A TCP port is a number (0-65535) that identifies a specific program or service on a computer, so incoming data reaches the right one.

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