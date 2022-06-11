"""
    String Method: istitle()
    ========================
    # Syntax : str.istitle()
    # istitle() doesn't take any parameters.
    # Return True, if the string is 'title_cased' string, else return False.
      e.g ----->   " Python Is Intresting"
      First characters of every word needs to be uppercase for 
      the string to be 'title_cased' string.
"""

# when all characters in a string is uppercase
p = "I AM  AWSOME"
print(p.istitle()) # return False

# when some characters are in uppercase
p = "I am AwsoME"
print(p.istitle()) # return False

# when all characters are in lowercase
p = "i know i m bad at programming till now "
print(p.istitle())

# when every word has it starting with uppercase 
p = "Python Is Fun"
print(p.istitle()) # return True

# when single word is passed 
p = "PYTHON"
print(p.istitle()) # return False