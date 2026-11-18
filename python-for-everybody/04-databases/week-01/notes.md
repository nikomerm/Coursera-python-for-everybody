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







                                                                **Tuesday 17/11/2026**

# DATABASES
# Basic Structure Query Language (SQL)**
**Relational Databases**

Databases in Programming

Databases are essential for storing and retrieving data efficiently, especially when dealing with large datasets or network limitations.
Using databases speeds up workflows by separating data retrieval from data analysis.
A database stores data in tables that are fast to search, sort, and connect. SQL is the language you use to talk to it.

Python & SQL are a powerful thing: Python cleans up the Data, SQL is a great way to store and retrieve Data.
SQL has 5 basic commands ( CRUD )
Create a table
Retrieve some Data
Insert Data
Update Data
Delete Data

**Using Databases with Python**

Database Model = Schema = Contruct
Is the contruct about the shape of what we're going to store and retrieve in our Database.
Common Database Systems : Oracle , MySql- open source, Sqlserver, PostGres, SQLite

Creating and Managing a Database

Use SQLite browser or similar tools to create a new database file that stores data in a specialized format optimized for fast retrieval and storage.
Create tables with a defined schema specifying column names and data types, which act as a contract for the data stored.

**Basic SQL Operations**

**SQL** INSERT
The insert statement inserts a row into a table

    keyword   table name   list of columns   Sql statement  coresponding values #name,email
    |    |    |              |                    |          |
INSERT INTO   Users      (name,email)             VALUES   ('nikos,mm@edu.gr)

**SQL** DELETE
Deletes a row in a table based on a selection criteria.

DELETE FROM Users WHERE email='mm@edu.gr'

**SQL** UPDATE
Allows the updating of a field with a where clause(μεταφραση= ρήτρα ή συνθήκη)

UPDATE Users SET name = 'Charles' WHERE email= csev@edu.com

Retrieving Records : SELECT
The select statement retrieves a group of records you can either retrieve all the records or a subset of the records with a WHERE clause.

SELECT * FROM Users
SELECT * FROM Users WHERE email = 'csev@edu.com'

Sorting with ORDER BY
You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order

SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name


                                                       **Wednesday 18/11/2026**
# Data Models and Relational SQL
**Designing a Data Model**

The concept of database design focusing on linking multiple tables together to efficiently store and manage data for applications.

Designing a Data Model : Plan your tables before writing code. A good design stores each piece of data once and connects tables with numbers (keys).
"You have to think , the thing that is the most essential to this application"

The Golden Rule

Never put the same string in the database more than once. If data repeats, move it to its own table and refer to it by a number.

Bad design (one table, repeated text):

track	artist	album
Thunderstruck	AC/DC	Razors Edge
Hells Bells	AC/DC	Back in Black

“AC/DC” is stored many times. That wastes space, and one typo creates a “different” artist.

Good design (3 tables, linked by keys):

Artist		                         Album		                                   Track	
id	name	                      id	title, artist_id	               id	title, album_id

The 3 Kinds of Keys

Key	                              Meaning	                                              Example

Primary key	                      unique number for each row	                          Artist.id
Foreign key	                      a number pointing to another table’s primary key	      Album.artist_id
Logical key	                      the real-world value you search by	                  Artist.name


The primary key is usually an auto-numbered INTEGER PRIMARY KEY.
Don’t use the logical key (like a name or email) as the primary key.
Why numbers? They are much faster to search and compare than text.


Relationships
One-to-many: one artist has many albums. Put the foreign key on the “many” side (Album.artist_id).
Many-to-many: students and courses. A student takes many courses, and a course has many students. You need a connecting table with two foreign keys:

# SQL
CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (user_id, course_id)
)