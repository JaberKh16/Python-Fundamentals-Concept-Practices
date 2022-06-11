'''
    # Use of type() function
    ==========================
    Python Built-in Function type(object/value) is used to get the datatype of specified object.
    Though Python is Dynamically Typed Object Oriented Language so, type(object) will returns the 
    Specified Object Class.
'''

# simply calling type fuction ---> type(object/value)
print(type(2)) # passed as value

# via declared variable
x = type(3) # passed as value
print(x)


# taking a list and checking its type
product = ["samsung", "apple", "motorolla"]
print(type(product))

# via declared variable with casting data_type user input
x = type(int(input("Integer :"))) # takes the user input
print(x)  # Returns itz data_type like  ---->  <class  'int'>

# by,default Python takes a input stream as 'string' type
x = input("Enter something:\n")
print(type(x))

# explictily convert the input to 'string' type
x = type(str(input("String :\n")))
print (x)

