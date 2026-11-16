# Task 2: Nested JSON with missing keys

# Trains: nested paths, .get(), dicts (real API data is often incomplete)

# python
# data = {"users": [
#     {"name": "Angel", "address": {"city": "Thessaloniki"}, "orders": [{"id": 1, "total": 25}, {"id": 2, "total": 40}]},
#     {"name": "Kallia", "address": {"city": "Athens"}, "orders": []},
#     {"name": "Mairi", "orders": [{"id": 3, "total": 10}]}
# ]}

# Write summarize_users(data, default_city):

# Loop through the users and, for each one, add up the total of all their orders.
# If a user has no address, use default_city. Use .get() so it doesn’t crash.
# Return a dict of name: (city, total_spent).

# Expected: summarize_users(data, "unknown") gives
# {'Angel': ('Thessaloniki', 65), 'Kallia': ('Athens', 0), 'Mairi': ('unknown', 10)}


data = {"users": [
    {"name": "Angel", "address": {"city": "Thessaloniki"}, "orders": [{"id": 1, "total": 25}, {"id": 2, "total": 40}]},
    {"name": "Kallia", "address": {"city": "Athens"}, "orders": []},
    {"name": "Mairi", "orders": [{"id": 3, "total": 10}]}
]}

def summarize_users(data, default_city):                      #Defines the function. data and default_city are parameters: slots that hold whatever you pass in at the call. Nothing runs yet.
    summary = dict()
    users_lst = data['users']                                #Reads the label 'users' from the big dictionary. The result is the list of 3 user dictionaries.
    for user in users_lst:                            #Outer loop. user holds one user dictionary at a time: first Angel’s, then Kallia’s, then Mairi’s. Everything indented below runs once per user.
        address = user.get('address', {})             #Gets the user’s address dictionary, or an empty {} if there isn’t one.
        city = address.get('city', default_city)      #Gets the city from that address, or default_city if there’s no city.
        total_spent = 0
        
        for order in user['orders']:        #Inner loop over this user’s list of orders. order is one order dictionary at a time, like {"id": 1, "total": 25}. For Kallia the list is empty, so the loop body never runs.    
            total_spent = total_spent + order['total']        
        summary[user['name']] = (city, total_spent)     #Runs once per user, after the inner loop, when the total is final. It adds one entry to the result box: the key is the user’s name, the value is a tuple (city, total_spent).             
    return summary                
        
print(summarize_users(data, "unknown"))    

