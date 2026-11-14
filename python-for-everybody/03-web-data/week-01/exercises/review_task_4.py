# Task 4: Validate incoming data and save it
# Trains: validation (what a backend does with every request), json.dump / json.load

# users = [
#     {"name": "Nikos", "email": "n@x.com", "age": 30},
#     {"name": "Maria", "age": 25},
#     {"name": "", "email": "g@x.com", "age": "abc"}
# ]

# Write validate_users(users, required_fields):

# Loop through the users. A user is invalid if a required field is missing, the name is empty, or age is not an int.
# Return two lists: valid (the good users) and errors (strings like "Maria: missing email").
# Then save valid to valid_users.json with json.dump(..., indent=4), read it back with json.load, and print it.

# Expected: 1 valid user (Nikos) and 2 error messages.

import json

users = [
    {"name": "Nikos", "email": "n@x.com", "age": 30},
    {"name": "Maria", "age": 25},
    {"name": "", "email": "g@x.com", "age": "abc"}
]

def validate_users(users, required_fields):
    errors = []                             #Two empty boxes, created once, before the loop. errors will hold texts (problems).
    valid = []                              #valid will hold dictionaries (good users). If they were inside the loop, each new user would wipe them.    
    for user in users:                      #Outer loop. user is one dictionary at a time: Nikos’s, then Maria’s, then the third. Everything indented below runs once per user.   
        is_valid = True                     #A flag: True or False. It starts as True (“assume fine”) for each user, and it’s inside the outer loop so it resets for every user. 
        for field in required_fields:       #Inner loop. field is one text at a time: "name", then "email", then "age". It runs once per field, for the current user.
            if field not in user:           #not in checks the labels of the dictionary user. It’s true when this label doesn’t exist. For Maria, with field = "email", it’s true.
                errors.append(user['name'] + ': missing ' + field)   #Runs only when a label is missing. The first line adds a text like 'Maria: missing email' to errors (the + joins pieces, and the space after missing is inside the quotes). 
                is_valid = False             #The second line flips the flag: this user has a problem.
        if user['name'] == "":                #Back at the outer-loop level (it lines up with for field), so it runs once per user, after the inner loop. user['name'] is text, and == "" asks if it’s empty. Note that the third user has the label name, so the not in check passes. That’s why this is a separate check.
            errors.append('name is empty')     #Adds the error text and 
            is_valid = False                     #flips the flag.
        if not isinstance(user['age'], int):      #isinstance(value, type) is true if the value is of that type. With not, it’s true when age is not a whole number. For "abc" it’s true.
            errors.append('age is not an int')
            is_valid = False
        if is_valid == True:                       #After all three checks, if the flag is still True, no check found a problem, so the whole user dictionary goes into valid.
            valid.append(user)            
    return valid, errors        

valid, errors = validate_users(users, ["name", "email", "age"])       #The call. users goes into the slot users, and the list of 3 texts goes into required_fields. The function returns a tuple of 2 lists, and this line unpacks it: the first goes into valid, the second into errors. The list is written here because required_fields exists only inside the function.
with open("valid_users.json", "w") as f:                             #Opens (or creates) a file for writing ("w" overwrites if it exists). f is the open file, and with closes it automatically when the indented block ends. The file lands in the terminal’s current folder.
    json.dump(valid, f, indent=4)                                     #Writes the Python data into the file as JSON text. Order: data first, then the file. indent=4 makes it readable. dump writes to a file, dumps makes a text.
print(errors)

with open("valid_users.json", "r") as f:                               #Opens the same file for reading ("r"). json.load (no s) reads JSON from a file and gives back Python data: here a list with one dictionary (Nikos). print shows it, which proves the save and load worked.
    loaded = json.load(f)
print(loaded)