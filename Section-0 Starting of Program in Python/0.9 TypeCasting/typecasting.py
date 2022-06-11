
'''

    Typecasting in Python
    ======================
    
    #   Can simply cast the data_type with the syntax : data_type(value/variable)
    #   TypeCasting possible with these primary datatypes -->  
    #           1. int with int
                2. int with float
                3. str(string) with str(string)

    Note -> chr() itself's a string for character type casting.
'''

# typecast float into integer
x = int(5) + int(5.55)
print(x) # returns an float 

# typecast integer with float
x =int(4)+float(5.5)
print(x) # returns an float 

# typecast the integer with chracter
x = str("asd") + chr(2) # int have ASCII value type character
print(x)

# typcasting a float to integer
y = 5.6
y1 = int(y) + 25
print(y1) # returns 30

# typecast the integer and the string literal
x = int("a") + str(5) # raises a ValueError
print(x)
