# Task 3: Call a real API safely

# Trains: urlencode, urlopen, error handling (the bread and butter of backend work)

# Use the same endpoint as the assignment: http://py4e-data.dr-chuck.net/opengeo?

# Write get_place(address):

# Build the URL and call the API.
# Return a tuple (formatted, lat, lon, plus_code) from the first result.
# If the JSON is broken or features is empty, return None instead of crashing (use try/except and a length check).

# Then loop through this list and print the result, or Not found for each None:

# python
# places = ["Irkutsk State University", "NYU", "asdfghjklqwerty"]

# Expected: Irkutsk gives plus_code 867FXG3R+M2, NYU starts with 87G7P, and the last one should print Not found.

import urllib.request, urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

def get_place(address):
    bouts = dict()
    bouts['q'] = address
    url = serviceurl + urllib.parse.urlencode(bouts)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    info = json.loads(data)
    return info

parms = ['features']


result = get_place("Irkutsk State University")
parms = result['features']
print(type(parms), len(parms))
#print(json.dumps(result, indent=4))

