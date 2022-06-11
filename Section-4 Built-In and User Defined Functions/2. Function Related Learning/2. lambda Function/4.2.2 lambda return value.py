
#to display the expression value need to call it through parameter
# print(x (2))
# we will learn it in the next part

# stated from here,


# with single arguments
# work with linear function with degree 1
x = lambda x : x**2 + 5
print(x(2)) # to get a value we need to call the lambda function

#work with polynomial with degree 2
x = lambda  x : x**2+ 4*x + 5
print(x(2))

#work with polynomial with  degree 3
x = lambda  x : x**3 + 2*(x**2)*1+ 2*(x)*1**1 + 1**3
print(x (6) )

# with double arguments
x = lambda  x, y : x**2 + 4*y + 15
print(x(2, 5))

# with triple arguments
x = lambda  x, y, z : x**2 + 4*y + z
print(x(2, 5, 4))

# nested lambda function
x = lambda c :lambda a, b : lambda e ,f, g : lambda y :( c*(a + b)/ e + (f- g))% y
print(x(2)(5, 6)(5, 2, 10)(12))
