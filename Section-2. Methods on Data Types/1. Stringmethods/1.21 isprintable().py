"""
    String Method: isprintable()
    ============================
    # Syntax : str.isprintable()
    # isprintable() doesn't take any parameters.
    # Return True, if all characters in the string are printable or
    the empty string, else return False.
    # Now the character which are printable in the screen are the following:

        1. letters and symbols
        2. digits
        3. punctuation
        4. whitespaces

"""

# white spaces are printable
p = "Space is a printable"
print(p.isprintable()) # return True

# empty string
p = " "
print(p.isprintable()) # return True

# when string have escape sequences with it
p = "i\a know\v\r im bad at\n programming\r\ntill\t now"
print(p.isprintable()) # return False

# alphanumeric string
p = "22PYTHON"
print(p.isprintable()) # return True


# working with if_else with typecasting
s = chr(27) + chr(97)
print(s) # prints whitespaces
if s.isprintable()==True :
    print("Printable.")
else :
    print("Not Printable.")


# when string itself a operation
s1 ="2+2 = 4"
print(s1) # prints similar string as specified
if s1.isprintable() == True :
    print("Printable.")
else :
    print("Not Printable.")

