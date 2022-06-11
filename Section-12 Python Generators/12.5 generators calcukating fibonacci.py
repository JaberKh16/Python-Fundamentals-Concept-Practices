"""
    Example Of Generator Calculation Fibonacci Series
"""

# defining the generator
def fibonacci_calcualtion_generator(number) :
    a = b =1
    for i in range(number):
        yield a
        a, b = b, a + b
        
for generates_values in fibonacci_calcualtion_generator(5):
    print(generates_values)