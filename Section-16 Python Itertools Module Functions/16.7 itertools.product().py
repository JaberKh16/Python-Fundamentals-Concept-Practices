"""
    itertools.product() Function
    ============================
    itertools.product() Function is used to creates a cartesian products
    from a series of iterables.    
    
    Syntax-
        itertools.product(*iterable)
        
            
"""

# importing the product() from the module
from itertools import product


# working with string data_type
str1 = "Message"
print(list(product(str1)))
print(list(product(str1, range(1, 2))))

# working with list data_type
list1 = ["Circle", "Rectangle", 1, "Pentagon", (1,4)]
print(list(product(list1)))
print(list(product(list1, range(2))))

# working with tuple data_type
tuple1 =(1, "a", "JK", (1, 2))
print(list(product(tuple1)))
print(list(product(tuple1, range(1, 2))))

# works with set data_type
set1 ={2, "a", "JK", (1, 2)}
print(list(product(set1)))
print(list(product(set1, range(1, 2))))

# working with dict data_type
dict1 ={2 : "a", "JK": (1, 2)}
print(list(product(dict1)))
print(list(product(dict1, range(1, 2))))
print(dict(product(dict1, range(1, 2))))


# working with dict data_type using tuple
dict1 ={2 : "a", "JK": (1, 2)}
print(tuple(product(dict1)))
print(tuple(product(dict1, range(1, 2))))

# working with dict data_type using str
dict1 ={2 : "a", "JK": (1, 2)}
print(str(product(dict1)))
print(str(product(dict1, range(1, 2))))

# working with dict data_type using set()
dict1 ={2 : "a", "JK": (1, 2)}
print(set(product(dict1)))
print(set(product(dict1, range(1, 2))))



