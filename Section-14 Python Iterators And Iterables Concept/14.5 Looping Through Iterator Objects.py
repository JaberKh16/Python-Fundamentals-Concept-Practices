"""
    [Iterator Object Accessing Using Loop]
    
    Iterator Object raise an exception named "StopIteration" if there has no 
    more data to access or all of its data is being iterated or accessed. 
    
"""

# declaring a list object
number = [2, 4, 5, 6, 7,8]

# making the list object an iterator using iter() method
i_numb = iter(number)

# accessin the iterator using loop
while True:
    
    try:
        # next(object) to get the next value of the specified object
        item = next(i_numb)
        print(item) # prints the object value

    except StopIteration:
        break