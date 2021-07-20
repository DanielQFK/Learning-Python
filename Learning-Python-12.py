# loop

# lopps are so useful and so important in Python , because it can stop doing something many times
# for example you want to write int-input for 20 times :(
# of course you can't so we use loop to do that :)
# we start with 'for' and we give it a variable e.g. 'x' and then in range(the number you want) with a :
# e.g. 
for x in range(20): 
    print('Python...')
# in output you will see 20 Python...

# But sometimes you want to print things those were in a list 
# e.g. 
our_list = ['daniel' , 'max' , 'jack' , 'jensen' , 'laura' , 'selena']
for i in our_list:
    print(i.title())
# in output you will see all names in the list

# Tip = Because the number start from zero in Python You should be careful if you want to print numbers from a loop , 
# start the number from 1 ...
for z in range(1 , 10):
    print(z)
# Even you can print numbers with 1 or 2 or ... space = 2 , 4 , 6 , 8 or 1 , 4 , 7 , 10 ...
# The third number is important in ()
# e.g. 
for t in range(1 , 50 , 3):
    print(t)
# tip = 3 is the space between numbers...   
