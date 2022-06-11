"""
    Try Except Block With Else 
"""

try :
    num1 = int(input("Enter a value for dividend:\n"))
    num2 = int(input("Enter the divisor:\n"))
    result = num1/num2
    
except ZeroDivisionError:
    print("Division by Zero.")
else :
    print("Result is : {}".format(result))