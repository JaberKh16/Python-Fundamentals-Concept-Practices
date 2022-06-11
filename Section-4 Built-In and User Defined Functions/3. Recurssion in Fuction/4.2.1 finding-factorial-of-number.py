""" 
    Recurssive Function Concept
    ===========================
    Recurssive Function is those type of function which calling itself
    and very useful when performing some sub tasks for the larger complex
    problem solving.
    
"""

# defining the function
def factorial_calculation(n) :
    # base condition
    if n ==1 :
        return n
    # recurssive condition
    else :
        return n * factorial_calculation(n-1)
    
# calling the function
print(factorial_calculation(5))
