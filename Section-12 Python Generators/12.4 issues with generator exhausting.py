"""
    Issues With Generator Exhausting Concept
    ========================================
    Calling the Generator the second time wont give anything. Because 
    the Generator Object is already exhausted and has to be re-initialized.
    For Example-

        #   Calling the generator again wont work.
            
            for i in generator_object:
                print(i) # returns nothing
        
    If you call next() over this iterator, a 'StopIteration' error 
    is raised.
    For Example-
    
        #   calling with next()
            
            next(generator_object)
            
    Approaches To Solve The Issue
    ==============================
    To overcome Generators exhausted issue three approaches can be followed
    which are the following-
    
    1)  Approach 1: Replenish the Generator by recreating it again and iterate over. 
        You just saw how to do this.
        For Example-
                def simple_generator():
                    x = 1
                    yield x
                generator_obj1 = simple_generator()
                generator_obj2 = simple_generator()
                generator_obj3 = simple_generator()
        
    2)  Approach 2: Iterate by calling the function that created the generator in 
        the first place.
        For Example-
                
            for i in simple_generator(): # 'simple_generator()' is the Generator
                print(i)
                
    3)  Approach 3 (best): Convert it to an class that implements a __iter__() method. 
        This creates an iterator every time, so you don’t have to worry about the 
        Generator getting exhausted.
        
        
"""
print("====================================================================")

print("# Approach-1: Replenish Generator by creating again")

print("====================================================================")

# # Approach-1: Replenish Generator by creating again
# def simple_generator():
#     x = 1
#     yield x
# generator_obj1 = simple_generator()
# print("From the Approach-1: ", next(generator_obj1))
# # print(next(generator_obj1))

# generator_obj2 = simple_generator()
# print("From the Approach-1: ", next(generator_obj2))


# generator_obj3 = simple_generator()
# print("From the Approach-1: ", next(generator_obj2))



try:
    # defining the generator 
    def simple_generator():
        x = 1
        yield x
        
    # Approach-1: Replenish Generator by creating again
    generator_obj1 = simple_generator()
    print(next(generator_obj1))
    generator_obj2 = simple_generator()
    print(next(generator_obj2))
    print(next(generator_obj2)) # here hits the exception
    
except StopIteration as error:
    print(error)

print("==============================================================================")

print("# Approach-2: Iterate by calling the function that returned the generator")

print("==============================================================================")

# Approach-2: Iterate by calling the function that returned the generator    
try:
    def generator_function() :
        for i in range (1,10) :
            yield i

    # assign the generator funciton into some variable
    generator_object = generator_function()
    
except Exception as error:
    print(error)
finally:
    # getting values via looping over the generator function
    for generates_values in generator_object:
        print(generates_values)
        
print("==============================================================================")

print("# Approach 3: Convert it to an class that implements a `__iter__()` method.")

print("==============================================================================")

# Approach 3: Convert it to an class that implements a `__iter__()` method.
class Iterable(object):
    def __iter__(self): # __iter__ method to create iterator every time
        x = 1
        yield x
        yield x + 1
        yield x + 2

# creating class instance
iterable = Iterable()

for i in iterable:  # iterator created here
    print(i)

for i in iterable:  # iterator again created here
    print(i)
    
print("==============================================================================")
