"""
    [Function Declaration With Return Statement Returning Multiple Values]
"""

# defining the function
def calculator(x, y):
    sum =x + y
    sub =x -y
    mul = x * y
    div = x / y
    return sum,sub, mul, div # returning multiple values

# calling the function and performing multiple assignment- single line assigment on multiple variables
p, q, r, s =calculator(10,3) # getting all the values from the function and assign into multiple variables
print("Sum is ", p)
print("Subtraction is ", q)
print("Multiplication is ", r)
print("Division is ", s)
