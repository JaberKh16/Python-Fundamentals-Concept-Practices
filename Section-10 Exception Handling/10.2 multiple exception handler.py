"""
    Handling Multiple Exception Example
"""

try :
    number = 20
    print(number + "message") # integer type concatenation with string type which is wrong
    print(number / 12)
    
except ZeroDivisionError:
    print("Divided by Zero.")

except(ValueError, TypeError): 
    # hits the 'TypeError' thus operation is applied to an object 
    # of incorrect type
    print("TypeError Occurred.")
