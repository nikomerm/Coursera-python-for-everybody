import sqlite3

conn = sqlite3.connect(":memory:")

def create_tables(conn):
    cur = conn.cursor() #explanation what this line does on every function in the end of the program
    cur.execute ('''
    CREATE TABLE books (id INTEGER PRIMARY KEY , title TEXT, author TEXT, year INTEGER)
    ''')
    cur.execute ('''
    CREATE TABLE members (id INTEGER PRIMARY KEY , name TEXT, email TEXT)
    ''')
    cur.execute ('''
    CREATE TABLE loans (id INTEGER PRIMARY KEY, member_id INTEGER, book_id INTEGER, loan_date TEXT, FOREIGN KEY (member_id) REFERENCES members(id), FOREIGN KEY (book_id) REFERENCES books(id))
    ''')
    conn.commit()         

def add_books(conn, books):    
    cur = conn.cursor()
    for book in books:
        cur.execute ('''
        INSERT INTO books (title, author, year) VALUES (?,?,?)''', book)
    conn.commit()


def get_books_by_author(conn, author):
    cur = conn.cursor()
    cur.execute ('''
        SELECT * FROM books WHERE author = ?''', (author,))
    return cur.fetchall()

create_tables(conn)
my_list = [
    ("Dune", "Frank Herbert", 1965),
    ("Dune Messiah", "Frank Herbert", 1969),
    ("Ouve", "Fredrick Backman", 2017),
    ("BearTown", "Fredrick Backman", 2019),
    ("Cathedrales", "Olivia Pineiro", 2020)                                                                        
]
add_books(conn, my_list)
print(get_books_by_author(conn, "Fredrick Backman"))

cur = conn.cursor()
cur.execute("INSERT INTO members (name, email) VALUES (?, ?)", ("Nikos", "nikos@example.com"))
cur.execute("INSERT INTO loans (member_id, book_id, loan_date) VALUES (?, ?, ?)", (1, 3, "2026-11-22"))
conn.commit()
cur.execute('''
SELECT members.name, books.title, loans.loan_date
FROM loans
JOIN members ON loans.member_id = members.id
JOIN books ON loans.book_id = books.id
''')
print(cur.fetchall())


# #explanation : Think of conn as the open database (the whole file or memory space where your tables live), and cur (the cursor) as a pen that writes and reads in it.

# conn = the connection. It can't run SQL itself. Its jobs are commit() (save changes) and handing out cursors.
# cur = the cursor. It's the thing that actually runs SQL (cur.execute(...)) and fetches results (cur.fetchall()).

# So cur = conn.cursor() means: "ask the connection for a cursor, and store it in the variable cur, so I can send commands through it."

# Why in every function? Each function only receives conn, and variables created inside one function don't exist in another.
# So each function makes its own cursor, uses it, and it disappears when the function ends. That's normal and cheap.

# A quick way to remember it: cur sends commands, conn saves them.







