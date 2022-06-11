'''
    # Syntax : str.isspace()
    # isspace() doesn't take any parameters
    # Returns  True , if character in the string have space;
    # Else  False return

'''

# white-space is given between a string 
p = " I am  working "
print(p.isspace())

# white-space is given between a string 
p = "M393onica Gr3347kkl"
print(p.isspace())

# a string with no character or having white-spaces
p = "   "
print(p.isspace())

# working with if_else condition
p = "Rar      "
print("Now checks with if_else condition :")
if p.isspace()==True :
    print("Have Space ")
else :
    print("Have no space")