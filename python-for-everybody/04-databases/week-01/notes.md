# 04-databases - Week 1

                                                        **Monday 16/11/2026**
# Using databases with Python
**Chapter Fourteen: Object Oriented Python**

Its a recall from what we learned in web-data Network Programms Part 2-3-4:

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

Before we send and before receive data , we have to encode and decode this stuff, so that it works out correctly.
The ord() function tells us the numeric value of a simple ASCII character. 

print(ord('H'))  #72

**code example:**

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0/r/n/r/n'.encode()     # (we send data so here encode is happening)
mysock.send(cmd)

While True:
    data = mysock.recv(512)
    if (len(data) <1 ) :
        break
    print(data.decode())                                                 # (we receive data so here decode is happening)
mysock.close()  



**Object Oriented Definitions and Terminology**

Key Concepts of Object-Oriented Programming:

Objects are self-contained units with data (attributes) and code (methods) inside, allowing users to interact without knowing internal complexities.
Programs are composed of multiple interacting objects, such as strings, lists, and dictionaries, which work together under the programmer's control.

**Classes, Instances, and Methods** :
A class is a blueprint or template defining the attributes and behaviors (methods) of objects but is not an object itself.
An instance (or object) is a concrete realization of a class, holding actual data and capable of performing methods defined by the class.
Methods are functions defined in a class that describe actions objects can perform; calling a method activates the associated code.

**Object Life Cycle:**

# Three stages:

Created (constructor), __init__
Used, by calling methods
Destroyed (destructor), __del__

Key points

Both the constructor and destructor are optional.
The constructor is very common. It sets up the object’s starting values.
The destructor is rare. You mostly need it when an object holds something that must be cleaned up.
Each object (instance) has its own copy of its attributes. Changing one doesn’t affect another.
self refers to the specific object being used.
An object is destroyed when nothing refers to it anymore. This happens when you reassign the variable (an = 42) or the program ends.
__init__ can take parameters, so you can customize each object when you create it.

# Example

python
class PartyAnimal:
    def __init__(self, name):
        self.name = name
        self.count = 0
        print(self.name, "constructed")

    def party(self):
        self.count += 1
        print(self.name, "party count", self.count)

    def __del__(self):
        print(self.name, "destructed")

a = PartyAnimal("Sally")   # constructed
b = PartyAnimal("Jim")     # constructed
a.party()                  # Sally party count 1
b.party()                  # Jim party count 1
a = 42                     # Sally destructed (no more references)

# Terms to remember

Class: the blueprint/template
Object / instance: a thing created from the class
Method: a function defined inside a class
Attribute: a variable that belongs to an object

Why it matters for the course: the later database examples (like Twitter/SQLite classes) use constructors to set up connections and attributes, so __init__ and self need to feel natural.

# Summary

**Class, Instance/Object, Constructor, Attribute, Method, Destructor** :

# Example :
class Dog:                         # class
    def __init__(self, name):      # constructor
        self.name = name           # attribute
        print(self.name, "is born")

    def bark(self):                # method
        print(self.name, "says woof")

    def __del__(self):             # destructor
        print(self.name, "is gone")


rex = Dog("Rex")           # instance (object)
bella = Dog("Bella")       # another instance
d = Dog("Rex")    # object created
d.bark()
d = None          # object destroyed

1. Class
The blueprint / template. It describes what a dog has (attributes) and does (methods), but it is not a dog itself.
class Dog: is the class. Think: “the recipe.”

2. Instance
One actual thing made from the class. Each instance has its own values.
rex and bella are instances. Think: “the cakes baked from the recipe.”

Instance = Object. In practice they mean the same thing. “Instance” just stresses which class it came from (“rex is an instance of Dog”).

2. Object
A real thing made from the blueprint (the class).
d = Dog("Rex"), so d is an object: one specific dog.

3. Constructor (__init__)
The code that runs automatically when the object is created. It sets up the starting values.
Think: “the birth of the dog.”

4. Attribute
A variable that belongs to the object. It stores information about it.
self.name is an attribute. Think: “the dog’s name tag.”

5. Method
A function that belongs to the object. It is something the object can do.
bark() is a method. Think: “the dog’s actions.”

6. Destructor (__del__)
The code that runs automatically when the object is destroyed (nothing refers to it anymore).
Think: “the dog leaves.”