"""
    [Function With Mulitiple Arguments Passing As Parameters]
"""

# defining the function
def calculator_operation(x, y, operator_sign):
    if(operator_sign=="+"):
        print("Sum is :", x+y)
    elif(operator_sign=="-"):
        print("Subtraction is :", x-y)
    elif(operator_sign=="*"):
        print("Multiplication is :", x*y)
    elif (operator_sign == "/"):
        print("Division is :", x / y)
    elif (operator_sign == "%"):
        print("Moduls  is :", x % y)
    else :
        print("Invalid Operation")

# calling the function with different arguments
calculator_operation(7, 5, "+")
calculator_operation(7, 5, "-")
calculator_operation(7, 5, "*")
calculator_operation(7, 5, "/")
calculator_operation(7, 5, "%")


