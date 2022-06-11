"""
    String Method: maketrans()
    ==========================
    # Syntax : str.maketrans( [ x, y [, z] )
    # maketrans() does take three parameters where y &  z are (optional)
    # maketrans is static method, that creates a 1-1 mapping of a
      character to it's translation or cay say replacement (unicode chr)
    #Simply say, unicode representation of each characters to it's
    translation (unicode chr) number,later which is use for mapping
    each character to it's corresponding (unicode chr) number
    # Now, about parameters,

      1.if one parameter(x) is given then it must have to dictionary
        data_type means (x) is only passed by a dict data_type
              e.g physically like  x=dict_type

      2. if two parameters(x, y) is being passed then it must have
          to be a string(str_type) with equal length
            mathematically, e.g  len(x)=len(y)
        here, each character of say, str1 is a replacement to it's
        corresponding index of str2

      3. if three parameters(x, y, z) is being passed each character
          in the say, str3 is mapped to None.

    # Note: if two or more characters are mapped in the dictionary, it
            raises an exception

"""

# when one parameter(x) is being passed
# Python say's it have to dict_ type
# It returns each string to its (unicode chr) number
dict1 ={"a" :"123", "b" :"456", "c" :"789"}
# same string_type in same length(str) of dict key's
str1 = "abc"
# different string_type in same length(str) of dict key's
print(str1.maketrans(dict1))
str2 ="def"
print(str2.maketrans(dict1))
# Also with different string_type in larger length(str) of dict key's
str3 ="defafqefag"
print(str3.maketrans(dict1))

# When dict key's are different data_type
# It returns (unicode chr) only for str_type keys
dict_type = {1: 2, 2:24, "a" : 23}
s = "asaf"
print(s.maketrans(dict_type))

# when two parameters(x,y) is being passed
# Pyhon say's it must be a two string
# say, x =str1, y =str2
# mathematically,len(str1)=len(str2)
# It returns str1 is mapped to it's corresponding str2 index(unicode chr)value

str1 = "abc"
str2 = "def"
print("Step -1 .Translation of string (abc): \n", str1)
print("Step -2 .Mapping with str2 corresponding index(unicode chr)number:\n",str2)
print("\n\nFirst work with s2 string reference(abc)")
s2 ="abc"  #reference str used for check
print("Now the string used for work with maketrans():\n",s2)
print("After The Mapping of str1 and str2 with s :\n",s2.maketrans(str1, str2))

print("\n\nSecond work with s1 string reference(abcffe)")
s1 = "abcffe" #reference str used for check
print("Now the string used for work with maketrans():\n",s1)
print("After The Mapping of str1 and str2 with s :\n",s2.maketrans(str1, str2))

# when three parameters(x, y, z) is being passed
# z parameter is the setter for y=str2 to None
# It also shows the  non existing substring mapped to None
# e.g  str1 = "abc", str2 ="def", str3 ="abdg" and ref. str ="absgc"
# z =str3 checks which substring isn't in the str1 is added
# -->as item to the dict making -->
##--> 1-10 to mapping in the dict , value leads to None , coz of setter(z)

str1 = "abc"
str2 = "def"
str3 = "abdg"
s = "absgc"
print(s.maketrans(str1, str2, str3))

