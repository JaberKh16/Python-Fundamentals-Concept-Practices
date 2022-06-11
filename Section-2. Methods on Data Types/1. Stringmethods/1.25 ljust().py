"""
    String Method: ljust()
    ======================
    # Syntax : str.ljust( width [ , fillchar])
    # ljust() does take two parameters.
    # Returns a (left-justified) string of given minimum width
    here, minimum width value must be >= to the specified string
    # Now, if the width value lesser than the specified string it will return 
    only the specified string.

"""
print("============================================================")
# When only the 'width' parameter is specified
s = "Fissy"
print(s)
width_value = 10
print(s.ljust(width_value))     # fits the string in range of width_value which is 10 here
                                # e.g -->  [f][i][s][s][y][][][][][]
                                # length of specified string is now 10
print("New Length is:", len(s.ljust(width_value)))


print("============================================================")
# 'width' is equal to the specified string
s1 = "Fissy"
width_value = 5;
print(s1.ljust(width_value))


print("============================================================")
# when both 'width' and 'fillchar' parameters are specified
s = "Fissy"
width_value = 10
fill_with_char = "*"
print(s.ljust(width_value, fill_with_char))

print("============================================================")