"""
    Printing Squires Of Number Using Generators 
"""

# Print squares of numbers from 1 to 10, using GENERATOR
def squares_of_numbers(numbers):
    for number in numbers:
        yield number*number

for i in squares_of_numbers([1, 2, 3, 5, 6]):
    print(i)