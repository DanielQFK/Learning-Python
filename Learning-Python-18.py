# set 2

# Adding Items to a Set

Days = {"Saturday" , "Sunday" , "Monday" , "Tuesday" , "Thursday"} 
print(Days)
Days.add("Friday")
print(Days)
"""Output:
{'Saturday', 'Sunday', 'Thursday', 'Monday', 'Tuesday'}
{'Saturday', 'Sunday', 'Thursday', 'Friday', 'Monday', 'Tuesday'}
"""


# Removing Items from a Set
"""There are two methods to do that..."""
# I continue the previous valuable abd its values (Days)
Days.remove("Saturday")
print(Days)
"""Output:{'Sunday', 'Monday', 'Friday', 'Tuesday', 'Thursday'}"""

Days.discard("Sunday")
print(Days)
"""Output:{'Monday', 'Friday', 'Tuesday', 'Thursday'}"""

Days.pop()
print(Days)
"""Output:{'Friday', 'Tuesday', 'Thursday'}"""

print(Days.pop())
"""Output:
Friday
"""



# clearing the set
Numbers = {0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10}
Numbers.clear()
print(Numbers)
"""Output:
set()
"""



# Set Union
Winter = {"January" , "February" , "March"}
Spring = {"Apr", "May", "June"}
Summer = {"July", "Aug", "Sep"}
Fall = {"Oct", "Nov", "Dec"}
All_seasons_mothes = Winter.union(Spring , Summer , Fall)
print(All_seasons_mothes)
"""output:
{'February', 'Dec', 'January', 'July', 'March', 'Aug', 'Sep', 'Apr', 'Nov', 'May', 'June', 'Oct'}
"""
a = {1, 2, 3}
b = {4, 5, 6}
c = {7, 8, 9}
all_numbers = a.union(b, c)
print(all_numbers)
"""output:{1, 2, 3, 4, 5, 6, 7, 8, 9}
"""

# or

print(Winter | Spring | Summer | Fall)
"""output:{'February', 'Dec', 'January', 'July', 'March', 'Aug', 'Sep', 'Apr', 'Nov', 'May', 'June', 'Oct'}"""

print(a | b | c)
"""output:{1, 2, 3, 4, 5, 6, 7, 8, 9}
"""



# Set Intersection
set1 = {1 , 2 , 3}
set2 = {3 , 4 , 5}
print(set1 & set2)
"""output:{3}
"""
# or

Intersection = set1.intersection(set2)
print(Intersection)
"""output:{3}
"""




# Set Difference
"""we continue with the "Set Intersection" valuables"""
print(set1-set2)
"""output:{1, 2}
"""
# or

Difference = set1.difference(set2)
print(Difference)
"""output:{1, 2}
"""
set3 = {1 , 2 , 3 , 4 , 5 , 6}
set4 = {4 , 5 , 6 , 7 , 8 , 9}
print(set3.symmetric_difference(set4))
"""output:{1, 2, 3, 7, 8, 9}
"""



# Set Comparison
set5 = {1 , 2 , 3 , 4 , 5 , 6}
set6 = {1 , 2 , 3 , 4 , 5 , 6}
Comparison1 = set5 >= set6
Comparison2 = set5 <= set6
print(Comparison1)
print(Comparison2)
"""output:
True
True""" 



# Length
set7 = {"max" , "jina" , "luara" , 2 , 123212221 , 4985748}
print(len(set7))
"""output:6"""




# Frozen Set
# Frozen Set is the same tuple so after creating you can't change it
set8 = frozenset([0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])
print(set8)
"""output:frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
"""
