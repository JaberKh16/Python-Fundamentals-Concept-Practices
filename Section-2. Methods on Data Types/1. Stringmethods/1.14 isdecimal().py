"""
    String Method: isdecimal()
    ==========================
    # Syntax : str.isdecimal()
    # isdecimal() doesn't take any parameters.
    # Returns True, if character in the string is decimal,else return False. 
    
    Basically, isdecimal() used to check whether a string is Decimal Number or not.
"""

# . is not decimal
n = "1234.325"
print(n.isdecimal())

# 'whitespace' is not decimal
n = "M393onica Gr3347kkl"
print(n.isdecimal())

n = "13137"
print(n.isdecimal())

# working with if_else condition
n = "12341413"
print("Now checks with if_else condition:")
if n.isdecimal()==True:
    print("Character all are Decimal.")
else:
    print("Character all are not Decimal.")