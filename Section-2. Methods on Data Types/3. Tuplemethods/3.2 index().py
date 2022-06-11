'''
    # Syntax : tuple.index(element)
    # index() does take a single parameter
    # Searches for the element in tuple and returns it index
    # If duplicate elements are present in tuple it returns the
      index of first occurrence of the matches substring
    # If searches element is not found is raises a ValueError exception
'''

#works with index()
tuple1 = (1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25})
print(tuple1)
print("Index no. = ", tuple1.index({32, 25}))
print(tuple1)
print("Index no. =",tuple1.index("JK"))
print(tuple1)
print("Index no. =",tuple1.index((1, 32)))
print(tuple1)




