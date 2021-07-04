# Lists in an easy way

# If you want to appned a high number , you may do thet with for ...
List = []
for x in range(31):
    List.append(x)
# print(List)

# But there is an easy way to append a high amount of numbers in list...
a = list(range(1 , 101))
print(a) 
# output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
# 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 
# 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# And this is to append only odd numbers...
b = list(range(1 , 101 , 2))
print(b)
# output = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
# 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

# And also this is the way to append even numbers...
c = list(range(0 , 101 , 2))
print(c)
# output = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
# 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]


#And ofcourse if you want to append exponent of a number you may do so...
d = []
for x in range(1 , 101):
    x = x**2
    d.append(x)
# print(c)    

# But there is an easy way to do that...
e = [x**2 for x in range(1 , 101)]
print(e)
# output = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 
# 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764,
#  1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721,
#  3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400,
#  6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]

# And when they ask you to print the minimum and the maximum of
# numbers in list you may do so...
f = [5 , 143 , 43 , 657 , 765 , 23 , 1]
f.sort() # Be carful to sort the list at first
# print(f[0])
# print(f[-1])
# for x in e:
#     x = x+x
# print(x)

# But there is an easier way to do it too...
print(min(f)) # output = 1
print(max(f)) # output = 756
print(sum(f)) # output = 1637

# Even when you want to print only numbers after of before a number...   
g = [2 , 4 , 2 , 7 , 54 , 7 , 4]
print(g[:3]) # output = [2, 4, 2]
print(g[3:5]) # output = [7, 54]
print(g[2:]) # output = [2, 7, 54, 7, 4]
print(g) # output = [2, 4, 2, 7, 54, 7, 4]
print(g[:]) # output = [2, 4, 2, 7, 54, 7, 4]

