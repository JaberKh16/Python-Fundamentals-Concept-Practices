'''
    # Syntax : list.index(element)
    # index() does take a single parameter
    # Searches for the element in list and returns it index
    # If duplicate elements are present in list it returns the
      index of first occurrence of the matches substring
    # If searches element is not found is raises a ValueError exception
'''

#works with index()
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25}]
print(list1)
print("Index no. = ", list1.index({32, 25}))
print(list1)
print("Index no. =",list1.index("JK"))
print(list1)
print("Index no. =",list1.index((1, 32)))
print(list1)




