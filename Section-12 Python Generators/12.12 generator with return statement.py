"""
    Generator With A return Statement
    ==================================
    Generator can have a 'return' Statement but that 'return'
    Statement doesn't need to return any value.

"""

# defining the generator function
def numberGenerator(n):
    if n < 20:
        number = 0
        while number < n:
            yield number
            number += 1
    else:
        return
print(list(numberGenerator(30))) # returns an empty list thus condition doesn't match