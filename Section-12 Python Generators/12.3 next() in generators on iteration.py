'''
    next() Method Concept With Generators
    =====================================
    # Iterable - is an object that enables programmer to access all
      contents over the container or iterables.
    # It has one built-in-method inside it
    # Method-   next()
    # next() methods helps you to get traverse through the container 
      contents one by one.
      e.g- means allow us to access the next element of a sequence/iterables
    # when reach out iterables last value next() method throws an exception
      saying 'StopIteration' and it happens because of bound over value.
'''
# defining the generator
def generator_function() :
    for i in range(1, 6):
        yield i
        
numbers = generator_function()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


print(next(numbers)) # hits the 'StopIteration' exception thus already reach last value
