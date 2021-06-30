# List 2
# Changing, Adding, and Removing Elements in List
# Sometimes you want to add or remove an element in your list so , 
# what should you do?
list = []

# Changing: 
list[0] = "Max"
# 0 = The number of the element in list.

# Adding:
# 1.
list.append("Max")
# append = add at the end of list.
# 2.
list.insert(0 , "Max")
# insert = add where ever you want in list.
# 0 = The number of the element in list.

# removing:
list.remove("Max")
list.pop(0)
del list[0]

