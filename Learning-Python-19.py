# Object-oriented programming
"""In Object-oriented programming(also known as OOP) , we use classes(to make charectors in some groups)
and mostly , they make it easier for us to write a program and it prevents writting many things repeatedly because you should also write
many method functions and that's why...
Tip = def is called 'method' in class """
# Now we should give them a valuable 

# Creating a Class 
class name: # class and # are musts
    def __init__(self, Your_name, Your_lastname): # metod init and self are also musts
        self.Your_name = Your_name
        self.My_name = Your_lastname

    def Height(self): # An optional method which you can use... it's not a must
        height = input("How tall are you? > ")
        self.height = height

    def Weight(self): # The same as the above
        weight = input("What is your weight ? > ")
        self.weight = weight
#Tip = Be careful to write 'self' ...


# To get output:
My_name = name("Emma" , "Mattew") # You should fill the vluables of __init__() (name and last name)
My_name.Height() #Now you call the method of Height
My_name.Weight() #And call the method of Weight
print(My_name.__dict__) # By __dict__ you print all info...
