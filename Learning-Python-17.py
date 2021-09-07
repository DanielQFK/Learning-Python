# set 
# Part 1

"""we can use set for numbers and strings 
How to Create a Set ?
1. Put anything(integers , strings ...) in curly braces {} and separate them with comma (,)"""
# tip:A set can hold any number of items(intege,string,even tuple...) and does not accept an element that is mutable(list , dictionary...)

# e.g.
from typing import List


Integer_set = {1 , 2 , 3 , 4 , 5 , 6 }
print(Integer_set)
"""
output:{1, 2, 3, 4, 5, 6 }
"""

String_set = {"Keira" , "John" , "Alexander" , "Bradly"}
print(String_set)
"""
output:{'Bradly', 'Alexander', 'John', 'Keira'}
""" 

Mix_set = {1 , "Liam" , [1 , 2 , 3 , 4 , 5]}
print(Mix_set)
"""
output:{1, 2, 3, 4, 5, 6}
{'Alexander', 'John', 'Keira', 'Bradly'}
Traceback (most recent call last):
  File "Learning-Python-17.py", line 20, in <module>
    Mix_set = {1 , "Liam" , [1 , 2 , 3 , 4 , 5]}
TypeError: unhashable type: 'list' 
"""

Mix_set = {1 , "Liam" , (1 , 2 , 3 , 4 , 5)}
print(Mix_set)
"""
output:{1, (1, 2, 3, 4, 5), 'Liam'}
"""
# We can also create a set from a list
List_set = set([1 , 2 , 3 , 4 , 5])
print(List_set)
"""output:{1, 2, 3, 4, 5}
"""
# Very very important tip: sets do not hold duplicate items
duplicated_set = set([1,2,3,4,3,2,1,1,2,3,4,4,3,2,1,1,1,1,1,1,1])
print(duplicated_set)
"""output:{1, 2, 3, 4}
"""

#To create an empty set in Python we must use the set() function without passing any value for the parameters (x = {} is not true because it can be dictionary)

# we can use loop for sets
loop_set = {1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}
for x in loop_set:
    print(x)
"""output:
1
2
3
4
5
6
7
8
9
10
"""
# We can also check for the presence of an element in a set using (in)
Check_set = {1 , 2 , 3 , 4 , "A" , "B" , "C"}
print("N" in Check_set)
print("A" in Check_set)
"""output:
False
True
"""

