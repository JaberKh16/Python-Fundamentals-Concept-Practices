"""
    String Method: strip()
    ======================
    # Syntax : str.strip([chars])
    # strip() does take a single parameter, but nothing can be passed if wanted.
    # Returns a copy of the string with leading and trailing
      characters being (removed) stripped out/remove from the specified string.
    # strip() removes characters passed as argument(chars).
    # If the argument 'chars' is not provided, default all leading and trailing
      whitespace are being removed from the string. But if specified then all 
      leading and trailing whitespaces along with the specified 'chars' is being 
      removed from the specified string.

"""

print("===============================================================")
# working with strip()
# with no argument is passed
r = "    this is good            "
print(r)
print(r.strip()) # reomves all leading and trailing whitespaces


print("===============================================================")
# when argument 'chars' is being specified
r = "  i am not good at all       "
print(r)
print(r.strip("i am not"))     # passing leading substring(chars)
print(r.strip("good at all"))  # passing trailing substring(chars)

print("===============================================================")

# working with leading and trailing substring via specifying argument 'chars'
website = "http://www.softwaretonic.com"
print(website)
print(website.strip("http://"))   # passing leading substring(chars)
print(website.strip("nic.com"))   # passing trailing substring(chars)


print("===============================================================")
# when passed a wrong 'chars' argument returns the same string as given
r = "    this is awsome           "
print(r)
print(r.strip('adefef'))  # wrong 'chars' is being passed as argument
print(r.strip("is ome"))
s