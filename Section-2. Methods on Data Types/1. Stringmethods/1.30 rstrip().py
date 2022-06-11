"""
    String Method: rstrip()
    =======================
    # Syntax : str.rstrip([chars])
    # rstrip() does take a single parameter, but nothing can be passsed if wanted.
    # Returns a copy of the string with trailing characters being (removed) stripped.
    # rstrip() removes characters starting from the right based on the argument 'chars' if specified
    # If the argument 'chars' is not provided, all trailing whitespace are
      being removed from the given string. But if specified then along with the
      specified 'chars' all trailing whitespaces is being removed from the specified string.

"""

print("================================================================")
# working with rstrip()
# no argument is passed
r = "this is good       "
print(r)
print(r.rstrip()) # reomves all leading whitespaces


print("================================================================")
# when argument 'chars' is being specified
r = "i am not good at all"
print(r)
print(r.rstrip("not good"))


print("================================================================")
# working with trailing substring via specifying argument 'chars'
website = "http://www.softwaretonic.com"
print(website)
print(website.rstrip("http://"))
print(website.rstrip("nic.com"))


print("================================================================")
# when passing 'chars' argument where specified 'chars' is having wrong substring 
# which will then return the given string.
r = "    this is awsome           "
print(r)
print(r.rstrip('adefef')) # wrong (chars) is being passed
print(r.rstrip("is ome"))

print("================================================================")