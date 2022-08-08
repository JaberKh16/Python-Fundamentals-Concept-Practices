'''
    Function Passed As Object To Another Function
    =============================================
    In Python, Function can be passed as another function as a object.
    
    For Example-
        sorted() is function inside a Python to sort out items
        in alphabetical or numerical order.
        
        sorted() function has argument named 'key' which is keyword
        argument which can takes a function object as argument.
            sorted(some_list, key=callable) # callable--> function_name
        
'''

# defining a function
def getting_sorted_order(fruits_list):
    # sorted() method 'key' basically takes a function object
    return sorted(fruits_list, key=make_lowercase)

def make_lowercase(fruits_list):
    return fruits_list.lower() # making all items in lowercase format


fruits = ['kumquat', 'cherimoya', 'Loquat', 'longan', 'jujube']
print(getting_sorted_order(fruits))