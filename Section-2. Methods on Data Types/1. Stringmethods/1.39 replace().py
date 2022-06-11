'''
    # Syntax : str.replace( [ "old", "new" [, count] )
    # replace()does take three parameters
    # Returns a copy of the string where all occurrence of a substring
      is replaced with another substring is passed as an argument
    # Here , "old"   --> which str u want to replace
             "new"   --> new substring which would replace the old string
             count --> the number of times want to replace

'''

#without count parameter
s = "Cold, Cold Heart"
print(s)
r = s.replace("Heart", "Hurt")
print(r)

#with count parameter
r = s.replace("Heart", "Heat", 2)
print(r)

c = "Let it be , let it be, let it be, let it be"
print(c)
r = c.replace("let", "don't let", 3)
print(r)
#It gives the original string because of maximum of 0 substring is replace
r = c.replace("let", "so", 0)
print(r)
