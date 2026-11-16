# Task 5: One simple XML task

# Trains: ElementTree, findall, converting XML to JSON (serialization between formats)

# python
# xml_text = """
# <products>
#   <product id="1"><name>Book</name><price>12.5</price></product>
#   <product id="2"><name>Pen</name><price>1.2</price></product>
#   <product id="3"><name>Bag</name><price>30</price></product>
# </products>
# """

# Write xml_to_list(xml_text, min_price):

# Parse the XML and loop through the product elements.
# Keep only products with price >= min_price (remember XML text is a string, so convert it).
# Return a list of dicts like {"id": 1, "name": "Book", "price": 12.5}, with id as an int and price as a float.

# Then print the result with json.dumps(result, indent=4).

# Expected: xml_to_list(xml_text, 10) returns Book and Bag only.

import json
import xml.etree.ElementTree as ET

xml_text = """
<products>
  <product id="1"><name>Book</name><price>12.5</price></product>
  <product id="2"><name>Pen</name><price>1.2</price></product>
  <product id="3"><name>Bag</name><price>30</price></product>
</products>
"""


def xml_to_list(xml_text, min_price):
  result = []
  tree = ET.fromstring(xml_text)  
  for product in tree.findall('product'):
    name = product.find('name').text
    price = float(product.find('price').text)
    if price >= min_price:
      product_id = int(product.get('id'))
      result.append({"id": product_id, "name": name, "price": price})     
  return result
      
    
print(json.dumps(xml_to_list(xml_text, 10), indent=4))