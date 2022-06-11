"""
    [Python DataType Related Numeric Built-in Functions]

    #   In Python, some built-in functions those are there to convert/typecast 
        the datatypes.
    #   Those Numeric functions are the following:

            1) int()   --> to cast to integer object/type
            2) float() --> to cast to floating point object/type
            3) str()   --> to cast to string object/type
            3) bool()  --> to cast to boolean object/type
            4) bytes() --> to cast to bytes object/type
            
"""

# convert a float to integer
num = int(3.4)
print("Convert Float To Integer:", num)

# convert a int to float
num = float(3)
print("Convert Integer To Float:", num)

# convert string to float with numeric value
num = float('3.4')
print("Convert String To Float with Numeric Value:", num)

# convert string to float with numeric value with arithmetical operator
num = float('-3.4')
print("Convert String To Float with Numeric Value with arithmetical operator :", num)

# convert integer to string
text = str('32')
print("Convert Integer To String:", text)

# convert numeric value to boolean
correct = bool(1)
wrong   = bool(0)
print("Convert Numeric Value To Boolean:", correct)
print("Convert Numeric Value To Boolean:", wrong)