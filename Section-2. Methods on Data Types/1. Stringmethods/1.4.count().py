"""
    String Method: count()
    ======================
    # Syntax : str.count( substring, (Opt)start=... , (Opt)end =...)
    # count() does take three parameters, atleast one which is 'substring' argument.
    # Returns the number of occurrences for the specified 'substring' arguments.
    # If three parameters have been passed, then it check for the substring
      within the range ( start= .. , end= ..)  specified and returns the
      occurrences for that substring.
"""

# with 'substring' parameter specified
str1 = "Ayesha  Asif Rangoonwala"
print(str1)
str2 = str1.count("s")
print("\n\nNumber of Occurrence for the substring (A)  :\n")
print(str2)


# with three parameter specified
str1 = "Ayesha  Asif Rangoonwala"
# print(str1)
str2 = str1.count("Aye", 0, -1)
print("\n\nNumber of Occurrence for the substring(Aye)  :\n")
print(str2)

# checking the length of the string
print("Length of the str1 :\n")
print(len(str1))
str3 = str1.count("a", 0, 24)
print("\n\nNumber of Occurrence for the substring (a) :\n")
print(str3)


