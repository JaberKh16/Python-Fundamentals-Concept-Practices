"""
    HCF(Highest Common Factor) Example
"""

# defining the function
def hcf(x,y):
    # gets the absolute of the number only 
    x=abs(x)
    y=abs(y)
    smaller = y if x>y else x
    s = smaller
    while s > 0:
        if x%s==0 and y%s==0:
            break
        s = s - 1
    return s

number_1 = int(input('Enter the first number:'))
number_2 = int(input('Enter the second number:'))

# pass the two number as argument
print(hcf(number_1, number_2))
