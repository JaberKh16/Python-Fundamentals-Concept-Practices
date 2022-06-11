"""
    String Method: rjust()
    ======================
    # Syntax : str.rjust( width [ , fillchar])
    # rjust() does take two parameters.
    # Returns a (right-justified) string of given minimum width
    here, minimum width value must have to be >= to the specified string to have 
    its effect. 
    # Now, if the width value lesser than the specified string it will return 
    only the specified string.

"""

print("============================================================")
# When only the 'width' parameter is specified
s = "Fissy"
print(s)
width_value = 10
print(s.rjust(width_value))     #fits the string in range of width in 10
                                # e.g -->  [][][][][a][y][e][s][h][a]
                                # length of specified string is now 10
print("New Length is:", len(s.rjust(width_value)))


print("============================================================")
# 'width' is equal to the specified string
s1 = "Fissy"
width_value = 5;
print(s1.rjust(width_value))


print("============================================================")
# when both 'width' and 'fillchar' parameter is specified
s = "Fissy"
width = 10
fillchar = "*"
print(s.rjust(width, fillchar))

print("============================================================")