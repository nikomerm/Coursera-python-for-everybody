# 02-data-structures - Week 3


                                                    **Wednesday 28/10/2026**
**Chapter 10: Tuples**
Tuples = πλειάδα. (computing: type  of data  structure) 
Στην πληροφορική: Δομή δεδομένων (συλλογή) που είναι αμετάβλητη (immutable) και διατηρεί τη σειρά των στοιχείων της. 
Στα μαθηματικά:Δομή δεδομένων (συλλογή) που είναι αμετάβλητη (immutable) και διατηρεί τη σειρά των στοιχείων της.
Tuples are a more efficient in terms of memory use and performance than lists. So in our program when we are making "temporary variables" we prefer tupples over lists.
Tuples are immutable. Unlike a list once you create a tuple you cannot alter its contents - similar to a string.

# Tuples Comparison:
Tuples in Python can be compared just like numbers or words. When you compare two tuples, Python looks at the first item in each tuple and decides which is smaller or larger. If the first items are the same, it moves on to compare the second items, then the third, and so on, until it finds a difference. Think of it like comparing two words in a dictionary: you look at the first letter, and if they’re the same, you check the next letter, and so forth.

For example, if you compare (1, 2) and (1, 3), Python sees that the first numbers (1 and 1) are equal, so it compares the second numbers (2 and 3). Since 2 is less than 3, (1, 2) is considered smaller than (1, 3). This way of comparing helps when sorting lists of tuples, like sorting names with scores, where the first item might be the name and the second the score.

# Comparing tuples
tuple1 = (1, 5)
tuple2 = (2, 3)
tuple3 = (1, 7)

print(tuple1 < tuple2)  # True because 1 is less than 2
print(tuple1 < tuple3)  # True because first items are equal (1 == 1), but 5 is less than 7
print(tuple2 > tuple3)  # True because 2 is greater than 1

# Sorting Lists of Tuples: Simple Explanation and Example

When you have a list of tuples, Python can sort the list by comparing the tuples one by one. It starts by comparing the first item in each tuple. If those are equal, it compares the second item, then the third, and so on. This makes sorting lists of tuples very natural and useful.
 
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 20)]   #List of tuples (name, age)


sorted_people = sorted(people)  **#Sort by name (first item), then by age (second item)**

print(sorted_people)

**OUTPUT:** [('Alice', 30), ('Bob', 20), ('Bob', 25), ('Charlie', 35)]

**The list is sorted first by the name alphabetically.**
**When names are the same (like "Bob"), it sorts by the age.**

If you want to sort by age first and then by name, you can create tuples with age first:

age_name = [(age, name) for name, age in people]  # Create a list with age first, then name


sorted_by_age = sorted(age_name)  **# Sort by age, then name**

print(sorted_by_age)

**OUTPUT:** [(20, 'Bob'), (25, 'Bob'), (30, 'Alice'), (35, 'Charlie')]

# 1.Sorting in Reverse Order
You can add the parameter reverse=True to the sorted() function to sort from highest to lowest:
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 20)]

 
sorted_reverse = sorted(people, reverse=True) **# Sort by name, then age, in reverse order**

print(sorted_reverse)

**OUTPUT:** [('Charlie', 35), ('Bob', 25), ('Bob', 20), ('Alice', 30)]

# 2.Using the key Parameter
The key parameter lets you specify a function that extracts a value to sort by. For example, to sort by age only:

sorted_by_age = sorted(people, key=lambda person: person[1]) **# Sort by age only**

print(sorted_by_age)

**OUTPUT:** [('Bob', 20), ('Bob', 25), ('Alice', 30), ('Charlie', 35)]

You can combine key and reverse:


sorted_by_age_desc = sorted(people, key=lambda person: person[1], reverse=True) **# Sort by age descending**

print(sorted_by_age_desc)

**OUTPUT:** [('Charlie', 35), ('Alice', 30), ('Bob', 25), ('Bob', 20)]

# 3.Sort by value the two methods

# Method 1: Using a for-loop with append 

d = {'a': 10, 'b': 1, 'c': 22}

temp = []
for k, v in d.items():
    temp.append((v, k))  # Create tuple (value, key) and append

temp_sorted = sorted(temp, reverse=True)  **# Sort by value descending**

for val, key in temp_sorted:
    print(key, val)

**Output:**
c 22
a 10
b 1

# Method 2: Using list comprehension (one-liner)

d = {'a': 10, 'b': 1, 'c': 22}

sorted_list = sorted([(v, k) for k, v in d.items()], reverse=True)

for val, key in sorted_list:
    print(key, val)

**Output:**
c 22
a 10
b 1

**Both methods:**

Create a list of (value, key) tuples to sort by value.
Use sorted() with reverse=True to sort descending.
Print the key and value in the original order.
The first method is more explicit and easier to follow step-by-step. The second method is more concise and preferred once you’re comfortable with list comprehensions.