'''
    Definition of Iterables
    =========================
    An Iterable is any Python object that is capable of returning 
    its members(items) one at a time, permitting it to be iterated 
    over in a loop.
    
    In simple word, An Iterable can be any Python object which 
    can be iterate upon. But to iterate over an Iterable it needs
    to converted into an Iterator.
    
    To make any Python Object an Iterator needs to use the __iter__()
    method, Once is created it is actually the Iterator that is being
    iterated. This is also what happends internally when we iterate over 
    using for loop. 
    
    Examples of Python Iterables are ---
    
        1. All Mutuable And Immutable Object...
            1.list  -- Imutable Sequential Object
            2.tuple -- Mutuable Sequential Object
            3.string -- Imutable Sequential Object
            4.dictionary -- Imutable Non-Sequential Object
            5.set -- Imutable Non-Sequential Object
    
    Any such Sequential and Non-sequential objects that can be iterated 
    through the for-loop.
    
    Even others Python Object
    
    Process --> 
        1.  All mutuable objects when we loop through that objects using for loop
            it called the (dunder or magic) method  __iter__() which then call
            its next() method to get the next value and by this __iter__()
            method makes mutable object an iterator.
            
    Note:   Any Python Object that has a dunder method __iter__() which means
            this object can be iterated upon thus making it an iterables.
            
            So, technically speaking, any Python Object that defines a 
            __iter__() method, is an iterable.  

'''

# now here's the list container or list iterable
nums = [1, 2, 3, 4]

for i in nums:
    print(i)

# checking whether this list has  __iter__() function or not
print(dir(nums))

# checking whether tuples has __iter__() function or not
co_ordinates = ((2, 4), (4, 5), (1, 4), (5, 8))
# print(co_ordinates)

# # to get the tuples value only
# for i in co_ordinates:
#     print(i)
    
# # to get the individual value for the tuples value
# for i in co_ordinates:
#     for j in i:
#         print(j)

print(dir(co_ordinates))


# list data structure is itself an Iterables not Iterator
# now checking either the list is itself is iterator or not
# it will show an TypeError: 'list' object is not an iterator
try:
    Colors = ["Black", "Red", "Blue", "Green"]
    # print(type(Colors))
    print(next(Colors)) # this will through an exception because list isn't a iterator
except Exception as error:
    print("Can't iterate like the iterator using next() method- 'list' is an iterable")

    
