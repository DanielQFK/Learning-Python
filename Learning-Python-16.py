"""Function

e.g.1
"""
def Defnumber1():
    print("Hello , how are you? ")

Defnumber1()
"""out put = Hello , how are you? """

"""as you can see it's just a simple def function
you can also return that...

def Defnumber1(): is function definition 
print("Hello , how are you? ") is docstring 
Defnumber1() is function call
Defnumber1 is parameter
and anything between () is argument"""

#Default Values
def Defnumber2(Name="Max" , Age=17):
    print(Name)
    print(Age)
    #both Max and 17 are Default Values
Defnumber2()
Defnumber2(Name="Emma") # that you can change it...
"""output = 
Max
17
Emma
17
"""

#Equivalent Function Calls
def Defnumber3(Name, Friend_name="John"):
    print(Name)
    print(Friend_name)
Defnumber3("Max")
"""output =
Max
John
""" 
Defnumber3("Willie")   
"""output =
Willie
John
"""
#IMPORTANT TIP = be careful to write the value of each one in the ()
# not Defnumber3()   ==>  Correct form : Defnumber3("Your name") 

# returning Function
def Defnumber4(a , b):
    c = a+b
    return c
Q = Defnumber4(2 , 3)
print(Q)   
"""Output:5"""  
# Tips = in returning , return something... 
# give a variable to your def and remember to write your numbers in () and print that variable  ...


# Function part 2

# Using a Function with a while Loop
def Def1():
    while True: # continues till uncountable amount
        print("Hello , how are you? ")
        answer = input(" > ")
        print("\nPlease say your name:")
        f_name = input("First name: ")
        l_name = input("Last name: ")

        Full_name = (f"{f_name}{l_name}")
        print(Full_name)
        break # It stops the while or if loop

Def1()

# Importing
"""At first , you should have the file you want to import in that folder you want to perform importing (sometimes you don;t have to)
then just write 
from [name of the file] import [The name of def function in that file]
from module_name import function_name
from module_name import function_0, function_1, function_2
"""

# Using as to Give a Function an Alias
"""from [...] import numpy as np
np()
np()
"""

#Importing All Functions in a Module
"""from [[name of the file]] import *  (* is important)
"""
