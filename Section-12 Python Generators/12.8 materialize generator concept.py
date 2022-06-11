"""
    Materialize Generator Concept
    ==============================
    We often store data in a list if you want to materialize it at some 
    point. If you do so, the content of the list occupies tangible memory. 
    The larger the list gets, it occupies more memory resource.
    
    Generators are memory efficient because the values are not materialized 
    until called and are usually faster. 
    
    You will want to use a generator especially if you know the logic to 
    produce the next number (or any object) that you want to generate.
    
    Can a generator be materialized to a list?
    -   Yes. You can do so easily using list comprehensions or by simply 
        calling list()
        
"""

# Print squares of numbers from 1 to 10, using GENERATOR
def squares_of_numbers(number=0):
    while number < 10:
        number = number + 1
        yield number*number

# for i in squares():
#     print(i)

# Materialise list from generator using list comprehension
materialised_list = [i for i in squares_of_numbers()] # using list comprehension iterate/materialise the Generator
print(materialised_list)

# # Materialise list from generator using list()
# materialised_list = list(squares())

# print(materialised_list)