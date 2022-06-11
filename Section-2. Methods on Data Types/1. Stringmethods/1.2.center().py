"""
    # Syntax : str.center( width[ , fillchar(Optional)])
    # center() have two parameters, does take atleast one while working.
    # Returns the string with padding with specified character e.g--> '   sdfd   '
"""

str1 = "i am awsome"
print(str1)

# with only 'width' parameter specified
str2 = str1.center(24)
print(str2)

str3 = str1.center(-24) # doesn't modify the string because of neg(-) width
print(str3)  # returns the same string which is given

# with 'fillchar' parameters specified
# filling with 'x' character where the string will be centerize with those fiiling characters
str2 = str1.center(24, "x") 
print(str2)
