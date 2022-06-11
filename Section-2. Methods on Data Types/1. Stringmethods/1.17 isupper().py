"""
    String Method: isupper()
    ========================
    # Syntax : str.isupper()
    # isupper() doesn't take any parameters.
    # Return True, if character in the string is uppercase, else return False.

"""

# when all character in a string is uppercase
p = "I AM  AWSOME"
print(p.isupper()) # return True

# when some characters are in uppercase
p = "I am AwsoME"
print(p.isupper()) # return False

# when no characters are in uppercase
p = "i know i m bad at programming till now "
print(p.isupper()) # return False
