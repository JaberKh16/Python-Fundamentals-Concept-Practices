"""
    String Method: index()
    ======================
    # Syntax : str.index(substring [ , start [, end]])
    # index() does take three parameters normally, but atleast single argument 'substring'  
      needed to specify to find that 'substring' index value.
    # Returns the index for the specified 'substring' which is being searched and then 
      returns the index value no. of that specified 'substring', else returns 
      the exception "ValueError": substring not found.  
    
    Basically, index() used to find out the index for a string object/sub string object.

"""

# Declaring String
quote = "Let it be , Let it be , let it be"
print(quote)
print("Length of the string :\n",len(quote) )

# When substring is in the string
r = quote.index("be")
print(r)

#Duplicate substring it returns the substring of the first occurrence

r = quote.find("Let")
print("Returning the first occurrence of the substring :\n",r)

#with three parameters
print("NOW with Three  Parameters :")
q = "Python is intresting , isn't it!!!!"
print(q)
print("Length of the string is :\n", len(q))
print(q.index("is intresting", 0, 30))
print(q.index("n't it", -10 , -1))
print(q.index("Python", 6, 20)) # raises an error when substring not in the range

#When substring isn't in the string
r = q.index("Java") # gives a ValueError exception
print("When substring not in the string :\n", r)

