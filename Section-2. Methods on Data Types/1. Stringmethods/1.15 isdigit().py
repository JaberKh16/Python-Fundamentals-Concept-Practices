"""
    String Method: isdigit()
    ========================
    # Syntax : str.isdigit()
    # isdigit() doesn't take any parameters.
    # Returns True, if character in the string is digit, else return False. 
    
    Basically, isdigit() used to find out whether a string is Digit or not.

"""

# . are not digit
n = "1234.325"
print(n.isdigit())

#white space are not digit
n = "M393onica Gr3347kkl"
print(n.isdigit())

n = "13137"
print(n.isdigit())

# working with if_else condition
n = "12341413"
print("Now checks with if_else condition :")
if n.isdigit()==True :
    print("Character all are Digit")
else :
    print("Character all are not Digit")