# Dictionary 2

#**In polls
Favotite_cars = {
    'Daniel':'BMW',
    'Ella':'Benz',
    'Max': 'Shevrolet'
}
Ella = Favotite_cars['Ella']
print(f"Ella's favorite car is {Ella} .")
#output = Ella's favorite car is Benz .
#Tip = Be careful to make a variable for that you want to put in {}

#**loop through Dictionary
"""to do that at forst make two variables to hold each one in the dictionary
then you should write 'item' at the end of line before () to make it work """
for name, car in Favotite_cars.items():
    print(name , car)
#output = Daniel BMW , Ella Benz , Max Shevrolet
#Tip1 = Be careful about ',' that is stuck to the first variable and be careful about item
for name in Favotite_cars:
    print(name)  
#output = Daniel , Ella , Max

#**Keys
for name in Favotite_cars.keys():
    print(name)    
#output = Daniel , Ella , Max

#**Values
for value in Favotite_cars.values():
    print(value)
#output = BMW , Benz , Shevrolet  


#**in order
Greeting = {
    'zack':'Hi',
    'john':'Hello',
    'Carl':'hi',
    'jack':'hello'
}
for name in sorted(Greeting.keys()):
    print("Hello" , name , ", How are you?")
#output = 
# Hello Carl , How are you?
# Hello jack , How are you?
# Hello john , How are you?
# Hello zack , How are you?

#** A list in Dictionary 
Dictionary = {
    'Name':'Daniel' ,
    'Books':['Math' , 'Science' , 'Literature']
}
print(f"My name is {Dictionary['Name']} , and these are my books:")
for Book in Dictionary['Books']:
    print(Book)
"""output = My name is Daniel , and these are my books:
Math
Science
Literature
"""

Students = {
    'Daniel' : {
        'Name':'Daniel' ,
        'Last_name':'TK' ,
        'Age':17 
    },
    'Max' : {
        'Name':'Max' ,
        'Last_name':'Amini' ,
        'Age':32
    } , 

}
for students, Their_info in Students.items():
    print(f'Students : {students}')
    Their_Info = f"Name : {Their_info['Name']} \n Lastname: {Their_info['Last_name']} \n Age :  {Their_info['Age']}\n" 
    print(f"Their information = \n {Their_Info}")
"""Output = 
Students : Daniel
Their information = 
 Name : Daniel 
 Lastname: TK 
 Age :  17

Students : Max
Their information = 
 Name : Max 
 Lastname: Amini 
 Age :  32
"""    
