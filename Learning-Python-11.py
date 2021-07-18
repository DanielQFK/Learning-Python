# tuple

# tuples are so similar to lists but with a defference 

# 1.You can change lists but you can't change touples
# 2.You write list in [] but you write tuple in ()

Tuple = ('alex' , 'max' , 'emma' , 'john')
print(Tuple)
# output = ('alex', 'max', 'emma', 'john')

print(Tuple[0])
# output = alex
print(Tuple[-1])
# output = john

Tuple1 = (100 , 324 , 534 , 54 , 123 , 342)
print(Tuple1)
# output = (100 , 324 , 534 , 54 , 123 , 342)

Tuple2 = (50 , 100 , 2)
print(Tuple2)
# output = (50, 100, 2)

Tuple3 = (300 , 5)
print(Tuple3)
# output = (300, 5)

# important tip:
# You can not append/insert/sort/remove or... tuples
Tuple3.append(23)
print(Tuple3)
# # output = 
# line 24, in <module>
#     Tuple3.append(23)
# AttributeError: 'tuple' object has no attribute 'append'
