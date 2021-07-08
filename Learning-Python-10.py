# if / elif / else

# if : conditions about something that if they were based on your
# condition something would be done or would be changed ...
# e.g.
number = 20 
if number>10:
    print("This is it... . ")
# Our condition was number (higher than 10) and as you can see it was so it prented what
# we wanted...

# e.g.2
Name = "Daniel"
if Name != "Alex":
    print("This is it... .")
# Attention = != means not equal to ...

# else : in case you want to say if something was not based on or was exept from what you 
# have said something else would be done or would be changed ...
# e.g.
Age = 18
if Age < 18:
    print("You don't have license...")
else:
    print("You have license... ")

# e.g.2 
Name = "Daniel"
if Name=="Daniel":
    print("Thats right...")
else:
    print("Oh no ...")
# Attention = == means something has the same thing or equal...    

# elif: it does something similar to if but with a difference which is 
# for example if the second condition(in your program) was true it would skip the third or ...
# conditions and would not follow the other , but in if , if the first condition was true 
# it would follow till the end of all ifs elifs and else ...

# e.g. 
Your_age = 19
if Your_age<16:
    print("You should pay 1 dollar ...")
elif Your_age<=19:
    print("You should pay 2 dollars...")
else:
    print("You should pay 5 dollars...")
# Attention = (<=) or (>=) means this is the same or more/less than... 


