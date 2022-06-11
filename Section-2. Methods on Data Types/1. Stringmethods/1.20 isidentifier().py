"""
    String Method: isidentifier()
    =============================
    # Syntax : str.isidentifier()
    # isidentifier() doesn't take any parameters.
    # Return True, if the string is valid identifier in Python Standard, else return False.
    # Valid Identifier has following properties:
        1) doesn't has any escape sequence(such as whitespaces, \n, \t, ..,etc) with it. 
        2) can't be start with numeric value.
        3) any kind of symbol
"""

# string is uppercase and has no whitespace
p = "IAMAWSOME"
print(p.isidentifier()) # return True

# having whitespaces in string 
p = "I am AwsoME"
print(p.isidentifier()) # return False

# having escape sequences at the end of the string
p = "iknowimbadatprogrammingtillnow\n\t"
print(p.isidentifier()) # return False


# starts with numeric value in string
p = "22Python"
print(p.isidentifier()) # return False

# starts with symbol characters in string
p = "@Python"
print(p.isidentifier()) # return False
