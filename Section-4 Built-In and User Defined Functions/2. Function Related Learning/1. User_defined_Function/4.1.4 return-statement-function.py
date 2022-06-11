"""
    [Function With Return Statement]
"""
# defining the function
def max_number(x, y, z):
    if (x>y and x >z):
        print("x is greater")
        return x

    elif(y>x and  y>z):
        print("y is greater")
        return y


    elif(z>x and z>y):
        print("z is greater")
        return z


    else:
        print("we are not in programm instruction")

# calling the function
print(max_number(10, 5, 2))
print(max_number(1, 2, 13))
print(max_number(2, 15, 3))

