"""
    String Method: translate()
    ==========================
    # Syntax : str.translate( translation_table )
    # translate() does take a single parameter which need to be passed. 
    # translate() method manually creates a maketrans() call
    # maketrans is static method, that creates a 1-1 mapping of a
      character to it's translation or cay say replacement (unicode chr)
    # Simply say, unicode representation of each characters to it's
    translation (unicode chr) number,later which is use for mapping
    each character to it's corresponding (unicode chr) number
    # Now, about parameters,

      1) translation_table --> contains the mapping between two characters
                              which is usually make by maketrans() call

"""

str1 = "abc"
str2 = "ghi"
str3 = "ab"
string = "abcdef"
print("Original String :", string)
trans = string.maketrans(str1, str2, str3)
print(trans)
print("In string =(abc) got the reference address in substring(c) of str1 ")
print("it gets the address because in str3 have removal substring(ab) of str3")
print("Translated String:", string.translate(trans))

print("\n\n\n\n\n")

str1 = "abc"
str2 = "ghi"
str3 = "abcd" # it removes the string as per as given
string = "abcdef"
print("Original String:", string)
trans = string.maketrans(str1, str2, str3)
print(trans)
print("In string =(abcd) got the reference address in string")
print("Translated String:", string.translate(trans))

# when translation_table is dict_type
# we can manually creates the translated table
trans = { 97 : None, 98 : None, 99: None}
print(trans)
string = "abcdef"
print("Original String:", string)
print("Translated String:", string.translate(trans))