'''
   # Python String DataType
   =========================
   #  String is a sequence of characters. It is a Text Type DataType.
   #  It is defined by value separated with double quote "" or single quote ''
   #  String can contains only String or Character DataType.
   #  String accessing can be done via Indexing.
   #  Arithmetical Operations like subtraction '-' and division '\' doesn't work
      with string it will give an error TypeError: Unsupported operand type(s).
   #  Any operation with operands is possible with String DataType but that will
      follow string logic.
   #  String is immutable which means string value can not be updated

'''

# Declared String DataType and then assigned into variable
x = " I am Awsome"
print(x)

# Concatenating the str1 with str2

str1 = "Ayesha Asif"
str2 = " Aangoonwala"
print(str1+str2)

# Repeting the string via multiplication (*) operator

str3 = str1*2
print(str3)

# Get The Length of the String using len(object)
str4 = "Hey are u there!! i m calling u!!"
print(len(str4))

# Concatenate two specified indexed Strings with '+' operator
str5 = "JK"
print(str5)
str6 = "Ayesha"
print(str6)
print(str5[0] + str6[5]) # returns  the concatenated indexed string

# Concatenatation of two String done via Slicing of two Strings
str5 = "JK"
print(str5)
str6 = "Ayesha"
print(str6)
print(str5[:-1] + str6[0 : 4]) # returns the concatenated slicing string


# Can not reassign- immutability check 
text= "Python String"
print(type(text))
text[0] = "J"  # not possible throughing an exception 
               # saying TypeError: 'str' object does not support item assignment
