""" 
    Class Based Iterator Defining
    =============================
    Two things to be reminded when making a class an iterator object
    which are the following-
    
    1) need to define __iter__() method to make the class an iterator object.
    2) need to define __next__() method so that this class iterator can be accessed.
    
"""

class MyRange :
    # class constructor function
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # defining the __iter__() dunder method to make an this class an iterator object 
    def __iter__(self):
        # though __iter__() itself creates a iterator object
        # so returning self is enough because we are making this
        # class to be an iterator.
        return self

    # now we need the __next__() to iterate through this iterator 
    def __next__(self):
        if self.value >= self.end: # condition of being exhausted
            raise  StopIteration
        current_value = self.value
        self.value +=1
        return  current_value

# creating the class instance
nums = MyRange(1, 10)
# we can also output the value through the next(methods)
# though now its an iterator because we made it through __iter__() method
print(next(nums)) # returns 1
print(next(nums)) # returns 2
print(next(nums)) # returns 3


print("------------------------------------------")
# now iterating rest values using the loop
for num in nums: 
    print(num) # returns 4, 5, 6, 7, 8, 9


print("-------------------------------------------")
print("-------------------------------------------")

# making generator for the same problem
# generator is similar like the function but work just as iterators
def my_range(start, end):
    current_val = start # current value 

    while current_val < end:
        yield  current_val
        current_val +=1

number = my_range(1, 10)
for numb in number:
    print(numb)
