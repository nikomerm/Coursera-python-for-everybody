# Task 2: Nested JSON with missing keys

# Trains: nested paths, .get(), dicts (real API data is often incomplete)

# python
# data = {"users": [
#     {"name": "Nikos", "address": {"city": "Thessaloniki"}, "orders": [{"id": 1, "total": 25}, {"id": 2, "total": 40}]},
#     {"name": "Kallia", "address": {"city": "Athens"}, "orders": []},
#     {"name": "Mairi", "orders": [{"id": 3, "total": 10}]}
# ]}

# Write summarize_users(data, default_city):

# Loop through the users and, for each one, add up the total of all their orders.
# If a user has no address, use default_city. Use .get() so it doesn’t crash.
# Return a dict of name: (city, total_spent).

# Expected: summarize_users(data, "unknown") gives
# {'Nikos': ('Thessaloniki', 65), 'Kallia': ('Athens', 0), 'Mairi': ('unknown', 10)}



def summarize_users(data, default_city):
    users = data['users']
    print(users)
    
data = {"users": [
    {"name": "Nikos", "address": {"city": "Thessaloniki"}, "orders": [{"id": 1, "total": 25}, {"id": 2, "total": 40}]},
    {"name": "Kallia", "address": {"city": "Athens"}, "orders": []},
    {"name": "Mairi", "orders": [{"id": 3, "total": 10}]}
]}

summarize_users(data, "unknown")