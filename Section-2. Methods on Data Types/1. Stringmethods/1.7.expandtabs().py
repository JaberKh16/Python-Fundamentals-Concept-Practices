""" 
    String Method: expandtabs()
    ===========================
    # Syntax : str.expandtabs(tabsize)
    # expandtabs() does take single parameters, no parameter passing can also work.
    # Returns a copy of string with all tab "\t" characters replaced with
      whitespaces.
    # By default tabsize is 8 depending on the IDEs.
    # If no parameters passes with expandtabs(), it returns the tab replaced
      string.
    # If expandtabs(2) ---> 2 4 6 8 ; Stopping index condition for the tabsize, 
      here expandtabs will be applied on every consecutive 2th index 
      thus 2 4 6 8 and so forth.

"""

# with no parameter specified
str1 = "Something\tis\tfissy\t1213\t"
print(str1)
str2 = str1.expandtabs()
print(str2)


# with parameters

str1 = "Something\tis\tFissy\t1213\t"
print(str1)
print("Tabsize(1) :", str1.expandtabs(1))
print("Tabsize(2) :", str1.expandtabs(2))
print("Tabsize(3) :", str1.expandtabs(3))
print("Tabsize(4) :", str1.expandtabs(4))
print("Tabsize(5) :", str1.expandtabs(5))



# No "\t" is given
str1 = "Something  is fissy."  # returns the same string bcoz no '\t' is given
str2 = str1.expandtabs()
print(str2)






