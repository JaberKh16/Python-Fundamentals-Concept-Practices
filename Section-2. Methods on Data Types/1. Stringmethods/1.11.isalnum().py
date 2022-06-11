"""
    String Method: isalnum()
    ========================
    # Syntax : str.isalnum()
    # isalnum() doesn't take any parameters.
    # Returns True, if the characters in the string is alphanumeric;
    (either alphabets or number) else return False.
    
    Basically, isalnum() used to check for the string is alphanumeric or not.

"""

# Declaring The String
n = "M1234onica"
print(n.isalnum())

# with whitespace which isn't alphanumeric
n = "M393onica Gr3347kkl"
print(n.isalnum())

n = "13137"
print(n.isalnum())

# working with if_else condition
n = "M094noicas244t"
if n.isalnum()==True :
    print("Character all are Alphanumeric.")
else :
    print("Character all are not Alphanumeric.")