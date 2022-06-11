"""
    String Method: split()
    ======================
    # Syntax : str.split( [separator [, max_split] )
    # split() does take two parameters, if wanted no parameter can be passed then 
    that case default separator whitespace is being considered when spliting is being 
    done means spliting is being done where whitespaces are being found.
    # Now, if argument 'separator' is being passed then that case spliting is being
    done where specified argument 'separator' is being found. Some Separators such 
    as (comma(,) colon(:), semicolon(;), substring, ...etc ). If any substring is being 
    passed as 'Separator' then that substring will be removed while spliting.
    # Another argument 'maxsplit' which is a number, which tells us to split the string into 
    maximum of provided number of times. If it is not provided then the default is -1 that 
    means there is no limit on the split.
    
    # Returns a List Type Data_Type from the String Data_Type.
    # It splits the string at the first occurrence of the substring
    (separator) string and returns a List.

"""

print("==============================================================")
# working with split() with no parameter
t = "Love thy neighbours"
print(t)
print("Length of the string :", len(t))

# when no parameters is being passed
# here, split() works on wherever whitespaces is being found
r = t.split()
print(r)

print("==============================================================")
# when 'separator' parameter is being passed returns string 
# where the 'separator' been removed form the specified string or can say
# replace with empty string [ '' ] if no string left after the spliting point
r = t.split("thy")
print(r)
r = t.split("thy neighbours")
print(r)


print("==============================================================")
# splits at ( "," ) str
e = "Milk, Chicken, Bread, Butter"
print(e)
r = e.split(",")
print(r)


print("==============================================================")
# splits on ":", returns the whole string with single list
e = "Milk, Chicken, Bread, Butter"
r = e.split(":")
print(r)


print("==============================================================")
# wokring with parameter 'max_split' is being specified
e = "Milk, Chicken, Bread, Butter"
print(e)
r = e.split(",", 2)
print("Max split at (2) :", r)

print("==============================================================")
# when wrong 'separator' is being passed and having parameter 'max_split' 
r = e.split("Chicken", 5)
print("Max split at (5) :", r)
r = e.split("Milk, Chicken", 25)
print("Max split at (25) :", r)
r =e.split("Milk, Chicken", 100)
print("Max split at (100) :", r)
r =e.split("Milk, Chicken", 3090)
print("Max split at (100) :", r)


print("==============================================================")
# with full of given string as (separator) parameters
r =e.split("Milk, Chicken, Bread, Butter", 3090)
print("Max split at (100) :", r)

r =e.split("Milk, Chicken, Bread, Butter", 10)
print("Max split at (10) :", r)

r =e.split("Milk, Chicken, Bread, Butter", 5)
print("Max split at (5) :", r)

r =e.split("Milk, Chicken, Bread, Butter", -5)
print("Max split at (-5) :", r)

print("==============================================================")
