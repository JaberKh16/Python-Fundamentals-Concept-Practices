'''
    Function Passed As Arguments Inside A Function
    ===============================================
    In Python, Functions can be passed inside a another function
    as arguments because functions are callable which makes it
    possible to passed functions as object inside a function.
    
    For Example-
        def function_name(func1, func2):
            return (func1(), func2())
        
        def func1():
            pass
        def func2():
            pass
        
        function_name(func1, func2)
        
'''

# defining a function to get the largest number
def find_largest_num(num_list):
    max_num = 0
    for val in num_list:
        if val > max_num:
            max_num = val
        else:
            continue
    return max_num

# defining a function to get the smallest number
def find_smallest_num(num_list):
    smallest_num = 999
    for val in num_list:
        if val < smallest_num:
            smallest_num = val
        else:
            continue
    return smallest_num

# taking two functions as arguments
def differentiate_max_min(find_largest_num, find_smallest_num, num_list):
    largest_num = find_largest_num(num_list)
    smallest_num = find_smallest_num(num_list)
    return (largest_num, smallest_num)


num_list = [10, 4, 1, 4, -10, 50, 32, 21, 42, -1]
print(differentiate_max_min(find_largest_num, find_smallest_num, num_list))

