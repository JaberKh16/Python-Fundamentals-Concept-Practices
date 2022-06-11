"""
    String Method: casefold()
    =========================
    # Syntax : str.casefold()
    # casefold() doesn't take any parameter.
    # Returns the string where all uppercase letters converts to lowercase letters.
    # Returns the same string if no uppercase letters found in specified string.
"""

# Creating String With First Letter In Uppercase
str1 = "Ayesha  Asif Rangoonwala"
print(str1)
str2 = str1.casefold()
print("\n\nComparing both string literals:\n")
print(str1)
print(str2)

# Creating String With All Letters In Lowercase
str3 = "this is not good"
print("\n\nComparing both string literals:\n")
str4 = str3.casefold()
print(str3)
print(str4)
