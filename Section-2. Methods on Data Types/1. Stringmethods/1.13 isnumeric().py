"""
    String Method: isnumeric()
    ==========================
    # Syntax : str.isnumeric()
    # isnumeric() doesn't take any parameters.
    # Returns True, if all characters in a string are numeric characters, else returns False
    # Numeric Characters has following properties:

        1. Numeric_type ---> Decimal ( 0, 12, 254266)
        2. Numeric_type ---> Digits  ( subscript, superscript)
        3. Numeric_type ---> Numeric ( fraction, roman numerals, currency numerator)
    
    Basically, isnumeric() used to find whether a string is Numeric or not.

"""

# Alphanumeric string
p = "222423"
print(p.isnumeric())


# Working with unicode checking with if_else condition
s = "\u00B225256"
if s.isnumeric()==True:
    print("Numeric")
else:
    print("Not Numeric")


# When string itself a operation
s1 ="2+2 ^^^ = @$4"
if s1.isnumeric() == True:
    print("Numeric")
else:
    print("Not Numeric")

# String is not numeric type
p = "Space is a printable"
print(p.isnumeric())

# Empty String is not numeric type
q = " "
print(q.isnumeric())

# When the string have escape sequences such as backslash escape sequence 
# which is not numeric
p = "i\a know\v\r im bad at\n programming\r\ntill\t now"
print(p.isnumeirc())