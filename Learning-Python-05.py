# List
# List is something that you can put many variables or integers in that in a particular order
# and when ever you want you can change the order or add or remove something from you List
# if you want to make a list you only need square brackets []
# e.g.
List = ["Learning" , "Python" , 3 ]      
print(List) 

# {or 
# List = ['Learning' , 'Python' , 3 ]                            
# print(List)}

# The output = [Learning , Python , 3 ]

# but you may not want to print all the list and just one of them
# so you have to write the name of list and the number
# of your command between square brackets 
# Tip1:the first item in list is considered as 0 in Python
print(List[0])

# the output would be = Learning
# even you can use title() and ... with them 
print(List[0].title())

# the second item in list is 1 and the third item is 3 and...
print(List[1])
#The output would be = Python

# but sometimes there are so many items in a list and you are unable to to count all 
# them to print the last item in a list .In this case , if you write -1 in [] it goes and print # the last item and in order -2 it print the previous item(the second from the end) and...

print(List[-1])
# the output would be = 3

