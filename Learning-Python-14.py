"""Dictionaries 

In this program we try to use dictionaries
In dictionaries you can give a same meaning or to write abbreviation or keyword of a long sentence instead of repeating it...

How to make?
1.Give a variable then = after that you should wrap in braces {}

e.g.1"""
Dictionary1 = {'Name':'Daniel' , 'Age' : 17}
print(Dictionary1['Name'])
print(Dictionary1['Age'])
"""Output:
Daniel
17
"""


"""
Tip = The string 'Name' is a key in this dictionary, and its associ­ated value is 'Daniel'
To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets
"""

"""You can also add to dictionaries"""
Dictionary1['friend'] = 'Max'
Dictionary1['teacher'] = 'Shayan'
print(Dictionary1)
#output = {'Name': 'Daniel', 'Age': 17, 'friend': 'Max', 'teacher': 'Shayan'}

"""It’s sometimes convenient, or even necessary, to start with an empty diction­ary 
and then add each new item to it"""

#e.g.2
Dictionary2 = {}
Dictionary2['Name'] = 'Emma'
Dictionary2['Age'] = 32
Dictionary2['brother'] = 'John'
print(Dictionary2)
#output = {'Name': 'Emma', 'Age': 32, 'brother': 'John'}

#**Modifting 
"""to do that , just write the kekword
and equal what you want to do
e.g.1"""
Dictionary1 = {'name':'max' , 'lastname':'amini'}
Dictionary1['name'] = 'Daniel'
print(Dictionary1)
#output = {'name': 'Daniel', 'lastname': 'amini'}


#**Deleting 
del Dictionary1['lastname']
print(Dictionary1)
#output = {'name': 'Daniel'}...
