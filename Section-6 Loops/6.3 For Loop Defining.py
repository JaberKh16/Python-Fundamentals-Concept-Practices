'''
    For Loop Concept
    ================
    # Syntax :  for var_name in iterable_name:
    # For Example;
        for x in range(start, end):
            print(x)
    
    # Some iterables are - list, rangem tuple, string, dictionary etc.
            
'''

# works with for loop with int_type var
x = 0
for x in range(1, 10, 1):
    print(x)

# works with for loop with int_type var reverse loop
x = 0
for x in range(10, 0, -1):
    print(x)


# works with for loop with int_type var
x = ""
for x in range(1, 5, 1):
    print("Hello Python")

# printing all even add and odd numbers
for x in range(1, 10, 1):
    if(x %2 ==0):
        print("Even Numbers :", x)
    elif(x %2 ==1):
        print("Odd Numbers :", x)
    else:
        print("Invalid Numbers")

# calculating sum for the first 10 int numbers
x =1
i =0
for x in range(1, 10):
    i=i+x
    print("Inside a loop Sum Visualization:", i)
print("Total Sum is :",i)
