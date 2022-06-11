"""
    String Method: lstrip()
    =======================
    # Syntax : str.lstrip([chars])
    # lstrip() does take a single parameter, but nothing can be passed if wanted.
    # Returns a copy of the string with leading characters being (removed) stripped.
    # lstrip() removes characters starting from the left based on the argument 'chars' if specified.
    # If the argument 'chars' is not provided, all leading whitespace are being removed
      from the given string. But if specified then along with the specified 'chars' all 
      trailing whitespaces is being removed from the specified string.
"""

print("==================================================================")
# working with lstrip()
# no argument is being passed
r = "      this is good"
print(r)
print(r.lstrip()) #reomves all  leading whitespaces


print("==================================================================")
# when arguemnt 'chars' is being passed
r = "i am not good at all"
print(r)
print(r.lstrip("not good"))


print("==================================================================")
# working with leading substring via specifying argument 'chars'
website = "http://www.softwaretonic.com"
print(website)
print(website.lstrip("http://"))


print("==================================================================")
# when passing 'chars' argument where specified 'chars' is having wrong substring 
# which will then return the given string.
r = "       this is awsome"
print(r)
print(r.lstrip('adefef')) # wrong (chars) is being passed
print(r.lstrip("s ti"))

print("==================================================================")