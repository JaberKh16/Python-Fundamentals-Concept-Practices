"""
    String Method: rsplit()
    =======================
    # Syntax : str.rsplit( [separator [, max_split] )
    # rsplit() does take two parameters,but if wanted no parameter can be passed then 
    that case default separator whitespace is being considered when spliting is being 
    done means spliting is being done where whitespaces are being found.
    # Returns a List Data_Type from given String Data_Type after the spliting.
    # It splits the string at the first occurrence of the substring
    (separator) string and returns a List.
    # This method splits the string starting form the right on the specified 'separator'.
    # It replaced the separator with '', if specified 'separator' is substring and nothing
    is being found/left after that specified substring.

"""
print("==================================================================")
# working with split()
t = "Love thy neighbours"
print(t)
print("Length of the string :", len(t))

# when no parameters is being passed
# split() works on whitespaces
r = t.rsplit()
print("With no parameter :", r)
print("==================================================================")


# when 'separator' parameter is being passed returns string 
# where the 'separator' been removed form the specified string or can say
# replace with empty string [ '' ] if no string left after the spliting point
r = t.rsplit("thy")
print("With separator :", r)
r = t.rsplit("thy neighbours")
print(r)

r = t.rsplit("Love thy neighbours")
print("With Full Str(separator) :",r)
print("==================================================================")



# splits at ( "," ) str
e = "Milk, Chicken, Bread, Butter"
print(e)
r = e.rsplit(",")
print(r)
print("==================================================================")


# splits on ":", returns the whole string with single list
r = e.rsplit(":")
print(r)
print("==================================================================")


# when parameter 'max_split' is being specified
e = "Milk, Chicken , Bread, Butter"
print(e)
r = e.rsplit(",", 2)
# when wrong 'separator' is being passed and having parameter 'max_split' 
print("Max split at (2) :", r)
r = e.rsplit("Chicken", 5)
print("Max split at (5) :", r)
r = e.rsplit("Milk, Chicken", 25)
print("Max split at (25) :", r)
r =e.rsplit("Milk, Chicken", 100)
print("Max split at (100) :", r)
r =e.rsplit("Milk, Chicken", 3090)
print("Max split at (100) :", r)
print("==================================================================")

r =e.rsplit("Milk, Chicken, Bread, Butter", 3090)
print("Max split at (100) :", r)

r =e.rsplit("Milk, Chicken, Bread, Butter", 10)
print("Max split at (10) :", r)

r =e.rsplit("Milk, Chicken, Bread, Butter", 5)
print("Max split at (5) :", r)

r =e.rsplit("Milk, Chicken, Bread, Butter", -5)
print("Max split at (-5) :", r)
print("==================================================================")



