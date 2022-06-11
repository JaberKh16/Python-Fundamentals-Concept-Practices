"""
    Generator Expression Concept
    ============================
    Generator Expression are like- List Comprehension but they returns
    a Generators instead of lists. Proposed in PEP 289, and became part 
    of Python since version 2.4.

    Syntax is similar to list comprehensions, but instead of square 
    brackets, they use parenthesis.
        
        
    Generator Expressions are useful when using reduction functions 
    such as sum(), min(), or max(), as they reduce the code to a 
    single line. They're also much shorter to type than a full 
    Python generator function. For Example-
    
            numbers = (x for x in range(10))
            print(sum(numbers))

"""

# writing the generator expression
numbers_list = (numbers for numbers in range(1, 11))
print(numbers_list) # returns the Generator Object

# to gets the values make it a list 
print(list(numbers_list)) # converts the generator into a list 

# genrator expression to reduce functions work in single line
numbers_list = (numbers for numbers in range(1, 11))
print(max(numbers_list)) # getting the maximum value from the generator expresion