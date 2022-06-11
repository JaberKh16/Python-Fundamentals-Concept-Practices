"""
    String Method: swapcase()
    =========================
    # Syntax : str.swapcase()
    # swapcase() doesn't take any parameters.
    # Returns a converted form of string of given string. If uppercase characters
    in the string then converted into lowercase and if lowercase then uppercase.
    # Simple words conversion goes like- uppercase into lowercase or lowercase into uppercase.

"""

# when  given string is in uppercase
p = "I AM AWSOME"
print(p)
print(p.swapcase())

# when given string is in lowercase
p = "i am awsome"
print(p)
print(p.swapcase())

# when given string is in mixed case
p = "i Am awSoME"
print(p)
print(p.swapcase())