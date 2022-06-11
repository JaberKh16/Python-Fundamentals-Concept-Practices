
'''
   # Python Boolean Datatype and Booleans Operators
   ================================================
   # In Python, it has two boolean values ('True' or 'False').
   # Python doesn't take ( 0 / 1) as True or False.

'''

'''
   # Some Comparison operators ---> such as ( == , != , >, < , >= , <= ) returns as Boolean value.
'''

'''
   #  Python have work on three boolean logic like other languages-
   #  Boolean Logical Operator are --- > ( and , or , not )
      a) and -- performs the logical '&$' operation
      b) or -- performs the logical '||' operation
      a) not -- performs the logical negation operation
      
   #  Other Python Membership Operator resulted boolean value such as
      the following --> in, is
      a) is    -- True if the operands are identical (refer to the same object)
      b) in    -- The in operator works with iterable types, such as lists or 
                  strings, in Python. It is used to check if an element is 
                  found in the iterable and then returns True if an element 
                  is found, otherwise returns False.

'''

# Working Booleans Values are -- True or False
have_id = True
print(have_id)

dont_have_id = False
print(dont_have_id)

# Working with Booleans Operator- ==, >, <, >=, <=, != 
x = print(2<1)
print(x)  # returns None
print(3==3) # retuns True
print(3 > 5) # returns False
print(4!=8) # returns True
print(5>=5) # returns True
print(5<=10) # returns True


# Working with Boolean Logical Operators
print(1==1 and 2==2)    # with 'and' operator
print(not 3 > 5)       # with 'not' operator
print(3>=5 or  10==10)  # with 'or' operator

# Work with Boolean Membership Operators- 'in'
# 'in' checks if particular element is present or not
fruits = ["Apple", "Orange", "Banana"]
print("PineApple" in fruits) # returns False
print("Orange" in fruits) # returns True
print("Strawberry" not in fruits) # returns False

if fruits is fruits:
   print("Both are identical.")