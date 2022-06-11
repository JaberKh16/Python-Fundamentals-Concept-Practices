"""
    We can pass an argument along with the Lambda Function.For that the syntax having a little bit change,
    Syntax --> (lambda x : x /2) (10) # needs to be enclosed with the parenthesis
    
    here, (lambda x : x / 2) is the Lambda Function
    and    (10) is the value or argument for this lambda function
"""

# Declaring and Passing an Argument
print((lambda x : x / 2 )(11))

# Declaring and Passing an Argument
print((lambda x: (2 + 3 * x ** 3) ** 2 + ((x+4) ** 4))(2))

