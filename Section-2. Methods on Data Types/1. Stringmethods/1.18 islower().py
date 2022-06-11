"""
    String Method: islower()
    ========================
    # Syntax : str.islower()
    # islower() doesn't take any parameters.
    # Return True, if characters in the string is lowercase, else return False.

"""

# when all characters in a string is uppercase
p = "I AM  AWSOME"
print(p.islower()) # return False

# when some characters are in lowercase and some are in uppercase
p = "I am AwsoME"
print(p.islower()) # return False

# when all characters are in lowercase
p = "i know i m bad at programming till now "
print(p.islower()) # return True
