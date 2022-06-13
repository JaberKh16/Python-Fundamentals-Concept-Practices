"""
    itertools.accumulate() Function
    ===============================
    itertools.accumulate() function makes an iterator that returns
    the result of a specified function.
    Syntax-
        itertools.accumulate(iterable [, func])
    
    accumulate() function normally does the accumulation if optional
    parameter [, function] has not been defined.
    
    Mechanism of accumulate() function is the following-
        
        data = [1, 2, 4, 5, 6]
        result = itertools.accumulate(data)
        
    Above code should be resulted as- 
        
        [1, 2]  ==> 1 + 2 = 3
        [3, 4]  ==> 3 + 4 = 7
        [7, 5]  ==> 7 + 5 = 12
        [12, 6] ==> 12 + 6 = 18
        
"""

# importing the itertools accumulate tool
from itertools import accumulate

print("==================================================")
print("Default Behavior Of itertools.accumulate() ")
print("==================================================")
# defining an iterable- list
data = [1, 2, 3, 4, 5]
result = accumulate(data)
print(result) # prints its a iterator object 

for value in result:
    print(value, end=',')

print("\n\n")

print("==================================================")
print("Default Behavior Of itertools.accumulate() ")
print("==================================================")

# defining an iterable - range() and then converted it to a list
nums = list(accumulate(range(1, 8))) # 1+2 = 3, 3+3 = 6, 6+4=10, 10+5=15, 15+6=21, 21+7=28   
print(nums)

print("\n\n")

print("==================================================")


from itertools import accumulate, takewhile, chain
# defining an iterable - list
nums = list(accumulate(range(1, 8)))
# print(nums)

print(list(takewhile(lambda  x : x <=6 , nums)))
print(list(chain(nums)))
print(list(chain(nums, range(1, 5))))

print("==================================================")