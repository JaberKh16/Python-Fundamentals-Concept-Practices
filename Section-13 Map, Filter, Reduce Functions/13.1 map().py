'''
    map() Function Concept
    ======================
    map() is a function that works as an iterator to return a result 
    after applying a function to every item of an iterable  such as
    -tuple, lists, etc. 
    
    It is used when you want to apply a single transformation function 
    to all the iterable elements.
    
    # Syntax -->
                    map(function, iterables)

    # it returns a new iterable with the function applied to each argument.

'''

# a simple programme without using map()
items = [1, 2, 3, 4, 5]
empty_list = [] #  an empty list
for i in items :
    empty_list.append(i **2 ) # appending the list 
    print("Inside loop work :",empty_list)
print(items)
print(empty_list)

print("\n\n\n")

# with function without using map()
def scroll_over_items():
    items = [1, 2, 3, 4, 5]
    empty_list = []
    for i in items:
        empty_list.append(i **2 )
    return  items, empty_list
print(items)
print(empty_list)
print(scroll_over_items())

print("\n\n\n")

# function with map()
def add_five(x):
    return x+5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums)) # maps the function with the iterables
print(result)
print(add_five(1))

# map() with lambda function
items = [1, 2, 3, 4, 5]
s = list(map(lambda x : x **2, items ))
print(s)

print("\n\n\n")

# list items of functions as argument in map()
def multiply_values(x):
    return (x*x)
def adding_values(x) :
    return (x +x)
func_of_list = [multiply_values, adding_values]
for i in range(1, 6):
    values = list(map(lambda x : x(i), func_of_list))
    print(values)

