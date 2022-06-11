"""
    String Method: endswith()
    =========================
    # Syntax : str.endswith( substring, (Opt)start=... , (Opt)end =...)
    # endswith() does take three parameters, but atleast one 'substring' argument
      need to specify.
    # Returns True or False for the specified 'substring' if ends with that specified substring.
    # If three parameters have been passed, it will check for the substring
      within the range ( start= .. , end= ..)  specified and returns
      True or False if it ends with that specified substring.

"""
# with 'substring' parameter specified
str1 = "I am going to say something"
print(str1)
str2 = str1.endswith("g")
print(str2)

str1 = "Now this is what i am going to say"
str2 = str1.endswith("i am going")
print(str2)


# with three parameters specified
str1 = "Something is very much fissy"
print(str1)


str2 = str1.endswith("very much fiss", 0, -1)
print(str2)
# print(str1[0:-1])


# checking the length for the string
print("Length of the str1 :\n")
print(len(str1))
str3 = str1.endswith("a", 0, 24)
print(str3)
