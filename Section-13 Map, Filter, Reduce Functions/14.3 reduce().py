'''
    reduce() Function Concept
    =========================
    reduce() function applies the function of two arguments cumulatively
    to the items of the list, from left to right, to reduce the list into
    a single value.

    Unlike the map() and filter() functions, the reduce() isn't a
    built-in function in Python. In fact, the reduce() function 
    belongs to the functools module.


    
    #   Syntax ---->
                reduce( function_name, iterable)

    #   it is useful function for performing some computation on a iterables
        like- list and returning the result.
    #   it applies a rolling computation to sequential pairs of values in a 
        list.

'''

# normal way of finding the product value of numbers
product = 1
list1 = [1, 2, 3, 4 ]
for num in list1:
    product = product * num
    print(product, end=",")
print("\n")
print("Final Summation is: ", product) # returns the last item which 24, though the iterator pointer points the last now 

# now working with reduce() function
# we need import it from functools though its function from that module
from  functools import reduce
product = reduce((lambda x, y : x*y), [1, 2, 3, 4])
print("\n")
print("Product of those numbers is: ",product)


# another example of working with reduce()
def summation_values(a, b):
    print(f"a={a}, b={b}, summation of {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(summation_values, scores)
print("Final Summation is: ", total)