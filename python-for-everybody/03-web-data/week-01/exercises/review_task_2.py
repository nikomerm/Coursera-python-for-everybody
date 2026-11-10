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

def summarize_users(data, default_city):
    summary = dict()
    users_lst = data['users']
    for user in users_lst:        
        address = user.get('address', {})
        city = address.get('city', default_city)
        total_spent = 0
        
        for order in user['orders']:            
            total_spent = total_spent + order['total']        
        summary[user['name']] = (city, total_spent)                  
    return summary                
        
print(summarize_users(data, "unknown"))    

