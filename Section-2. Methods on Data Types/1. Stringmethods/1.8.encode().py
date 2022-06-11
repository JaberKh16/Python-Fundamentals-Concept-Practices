"""
    String Method: encode()
    =======================
    # Syntax : str.encode([encoding =("utf-8"/ "ascii") , error = "strict"])
    # encode() does take two parameters(encoding, error )
    # By default, encode() doesn't require any parameter.
    # Returns a encoded version of the specified string.
    # In case of failure it raises an exception "UnicodeDecodeError"
    # Python supported this two type encoding   "utf-8" or "ascii"
    # About Errors:     1.strict
                        2.ignore
                        3.replace
                        4.xmlcharrefreplace
                        5.backslashreplace
                        6.namereplace
"""

# with no parameter specified
str1 = "Something\is\tFissy\r1213\n"
print(str1)
str2 = str1.encode()
print(str2)


# with  parameters specified
str1 = "Something\tis\Fissy\r1213\r\n"
print(str1)
print("The encode version (with 'replace') :", str1.encode("ascii", "replace"))
print("The encode version (with 'ignore')  :", str1.encode("ascii", "ignore"))
print("The encode version (with 'xmlcharrefreplace') :", str1.encode("ascii", "xmlcharrefreplace"))
print("The encode version (with 'namereplace') :", str1.encode("utf-8", "namereplace"))



# with no escape sequence
str1 = "Something  is fissy."  #returns the same string bcoz no '\t' is given
str2 = str1.encode()
print(str2)






