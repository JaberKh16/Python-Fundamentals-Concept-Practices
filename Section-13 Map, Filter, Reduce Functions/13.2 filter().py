'''
  filter() Function Concept
  =========================
  filter() Function can be applied to an iterable such as a list or 
  a dictionary and create a new iterator. 
  
  This new iterator can filter out certain specific elements based on 
  the certain condition. 
  
  # Syntax --->
                  filter(function_name, iterable)
                  
  # it filters out the iterable by matching with expression and return
    a Boolean value either true or false.

'''

# working with lambda using filter()
nums = [11, 22, 33, 44, 55]
r = list(filter(lambda x : x%2 ==0 , nums)) # filtering out the even numbers from the iterable
print(r)

# another example
numb_list = range(-5, 5)
r = list(filter(lambda x : x <0, numb_list))
print(r)

# working with user_defined_function
def lesser_than_zeros(x):
    return x < 0
numb_list = range(-5, 5)
less_than_zero = list(filter(lesser_than_zeros, numb_list)) # filtering the values which are lesser than 0 from the given range
print(less_than_zero)



