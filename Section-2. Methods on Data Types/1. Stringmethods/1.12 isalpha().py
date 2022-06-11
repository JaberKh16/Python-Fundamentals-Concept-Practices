"""
    String Method: isalpha()
    ========================
    # Syntax : str.isalpha()
    # isalpha() doesn't take any parameters.
    # Returns True, if characters in the string is alphabets, else return False.
    
    Basically, isalpha() used to check for the string whether it is alphabet or not.

"""

# Declaring The String
n = "Monica"
print(n.isalpha())

# with space which isn't alphabets
n = "Monica Gellen"
print(n.isalpha())

n = "13137"
print(n.isalpha())

# working with if_else condition
n = "M094noicas244t"
if n.isalpha()==True :
    print("Character all are Alphabets.")
else :
    print("Character all are not Alphabets.")