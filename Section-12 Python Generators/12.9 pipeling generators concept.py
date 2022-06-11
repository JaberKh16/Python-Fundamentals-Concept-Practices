"""
    Pipeline Generators Concept
    ===========================
    Multiple Generators can be pipelined(one generator using another) as 
    a series of operations in the same code. 
    
    Pipelining also makes the code more efficient and easy to read. 
    For pipeling functions, use ()paranthesis to give function 
    caller inside a function.
    
"""

# Generate odd numbers by pipelining generators
def generating_numbers(numbers):
    for number in range(numbers): # to generate numbers from 0 to 9
        yield number

def generating_odd_num(generating_numbers):
    for number in generating_numbers:
        if number % 2 == 1: # to generate the odd number
            yield number

# iterate over the pipeling generators
for values in generating_odd_num(generating_numbers(10)):
    print(values)