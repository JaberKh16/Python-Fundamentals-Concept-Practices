"""
    String Method: find()
    ======================
    # Syntax : str.find(substring [ , start [, end]])
    # find()/rfind() have similar type syntax property.
    # Both of them take three parameters at most, generally take a single argument 'substring'.
    # Returns the index value of first occurrence of the specified 'substring', simply saying,
      it gives the index no. for that specified 'substring', else return -1 , if that specified 
      'substring' isn't been found.

"""

# Declaring String
quote = "Let it be , let it be , let it be"
print(quote)
print("Length of the string :\n",len(quote) )

# When specified 'substring' is in the string
r = quote.find("be") # returns the first occurence index value for this specified 'substring'
print(r)

# When specified 'substring' isn't in the string
r = quote.find("aer")
print("When substring not in the string :\n", r)

# If Duplicate Substring is being found, it returns only the substring of the first occurrence
r = quote.find("let")
print("Returning the first occurrence of the substring :\n",r)

# with three parameters specified finding 'substring' in specified range
print("Now, with Three Parameters :")
q = "Do small things with great love"
print(q)
print(q.find("small things", 10))
print(q.find("small things ", 2))
print(q.find("o small", 10 , -1))
print(q.find("things", 6, 20))

# can do the same for the rfind()
print("Now this is about the rfind() string method:\n\n")
print("The String given is :\n\n")
q = "Do small things with great love, love"
print(q)
print(q.find("small things", 10))
print(q.find("small things ", 2))
print("Length of the string :\n", len(q))
print(q.find("love", 0, 36))
print(q.find("o small", 10 , -1))
print(q.find("things", 6, 20))

