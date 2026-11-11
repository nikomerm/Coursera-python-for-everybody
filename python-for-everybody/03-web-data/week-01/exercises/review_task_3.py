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

def get_place(address):                                  #Summary  Task 3 . This Function does : 
    bouts = dict()                                       # builds a URL from a parameter,
    bouts['q'] = address                                 #calls an API,
    url = serviceurl + urllib.parse.urlencode(bouts)     #survives broken JSON (try/except),
    uh = urllib.request.urlopen(url)                     #survives an empty result (len(...) == 0),
    data = uh.read().decode()                            #is used inside a for loop.
    try:                                                 #That is a real backend pattern.
        info = json.loads(data)
    except:
        return None

    features = info['features']
    if len(features) == 0:
        return None
    first = features[0]
    props = first['properties']
    formatted = props['formatted']
    lat = props ['lat']
    lon = props['lon']
    plus_code = props['plus_code']
    return formatted, lat, lon, plus_code

places = ["Irkutsk State University", "NYU", "asdfghjklqwerty"]
for place in places:
    answer = get_place(place)
    if answer is None:
        print('Result: Place Not Found')
    else:
        print('Result: ', answer)




