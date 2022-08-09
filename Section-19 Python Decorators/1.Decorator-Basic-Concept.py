'''
    Decorator Basic Concept
    =======================
    Decorator is a function that accepts a function and returns 
    a function.
    
    For Example: Consider a the following program
    >>> def is_prime(passed_number):
            for num in range(2, passed_number//2):
                if passed_number % n == 0:
                    return False
            else:
                return True 
    >>> is_prime(52525235) # returns some result after a while
    
    Now, when we call the same function with the same number it again
    perform the calculation and then returns with a result after some
    time.
    >>> is_prime(52525235)
    
    We would like to speed up the calculation process of is_prime() function
    and for that we can use Python built-in module 'functools' one decorator
    'lru_cache'. 'lru_cache' decorator accepts a function and returns a new 
    function that wraps around the original function:
        >>> from functools import lru_cache
        >>> is_prime_number = lru_cache(is_prime)
        
    The 'lru_cache' decorator returned a new function object to which we're 
    pointing our 'is_prime_number' variable to. When we call this new function, 
    the new function calls our original is_prime() function (which we had passed 
    to lru_cache) and it caches the return value for each argument that it sees.

    Every time this new function is called, it stores the inputs (the given function 
    arguments) and the output (return value) that corresponds to those inputs.
    
    This way of using decorator is bit unusual instead to use a decorator we
    use a special symbol like- @ to define the decorator.
    
'''

# importing the 'lru_cache' from functools
from functools import lru_cache

# defining the decorator
@lru_cache
def is_prime(passed_number):
    for n in range(2, passed_number // 2 ):
        if passed_number % n == 0: # not a prime number condition
            return False
    else: # its a prime number
        return True

# checking the is_prime() function will see returns a function object 
# basically nothing but a callable object. 
print(is_prime) # returns a callable object <functools._lru_cache_wrapper object at 0x7f735dc8fc10>
is_prime_number = is_prime(2242452)
print(is_prime_number)