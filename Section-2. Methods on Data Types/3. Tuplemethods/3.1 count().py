'''
    # Syntax : tuple.count(element)
    # count() does take single parameter
    # Searches for the element in tuple and returns the number
      of the occurrence of the element
    # If searches element is not found it returns 0
'''

#works with count()
# returns the number of occurrence for the substring(element)
tuple1 = (1, "a", "JK", (1, 5.33, "c"), "Ayesha",{32, 25} )
print(tuple1)
print("Occurence of {32, 25} : ", tuple1.count({32, 25}))
print(tuple1)
print("Occurence of (JK) : ",tuple1.count("JK"))
print(tuple1)
print("Occurence of (1,32) : ",tuple1.count((1, 32)))
print(tuple1)

print("\n\n\n\n")

#When duplicate substring(element) is found
l = (1,2, 4, 3, 6, 3, 7, 3, 3, 3 ,6)
print(l)
print("Occurence of 3 : ", l.count(3))
print(l)

#when pass the element not in the list
#returns 0 by default
print("Occurence of ggaff : ", l.count("ggaff"))
print(l)



