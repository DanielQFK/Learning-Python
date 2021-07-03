# Organizing a List
# How to orgnize a list in order ?

List = [2 , 4 , 1 , 3]
# 1.
# using .sort() to sort numbers in order or alphabetical order (permanently)
# e.g. 
List.sort()
print(List)
# output => [1 , 2 , 3 , 4]

# 2. 
# if you want to sort in reverse
List.sort(reverse=True)
print(List)
# output => [4 , 3 , 2 , 1]

# 3.
# but if you want to sort in order only for a short time (temporary)
print(sorted(List)) # = this command is only for once , just for once it sorts
# output => [1 , 2 , 3 , 4]

# 4.
# but if you only want to reverse 
List.reverse()
print(List)
#but be careful that this command does not reverse in order = it just reverses what in list are
# output => [3 , 1 , 4 , 2]

5.
# and in the end , if you want to calculate Length of a List:
print(len(List))

