# python Json methods
# Here's a table showing Python objects and their equivalent conversion to JSON.

# Python	JSON Equivalent
# dict	object
# list, tuple	array
# str	string
# int, float, int	number
# True	true
# False	false
# None	null

# Note:  the creating json is attaching list  dict or string to dict
import json
 
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

print("=================================================1")

x = {"name": "John",
  "age": 30,
  "city": "New York"}
# convert into JSON: 
# use four indents to make it easier to read the result:
y=json.dumps(x,indent=3)
print(y)

print("=================================================2")
#  Python read JSON file
# with open('path_to_file/person.json', 'r') as f:
#   data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print(data)

print("=================================================3")

# Writing JSON to a file
person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}
with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)
print(person_dict)  


