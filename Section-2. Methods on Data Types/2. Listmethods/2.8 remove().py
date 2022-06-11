'''
    # Syntax : list.remove(element)
    # remove() does take single parameter
    # Searches for the element in list and removes
      the first matching substring(element)
    # If duplicate elements are present in list it removes the
      first occurrence of the matches substring
    # It doesn't return any value , returns None
    # If searches element is not found is raises a ValueError exception
'''

#works with remove()
#list.removes returns None
#None means absence of value
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25}]
print(list1)
print("Removal of  = ", list1.remove({32, 25}))
print(list1)
print("Removal of =",list1.remove("JK"))
print(list1)
print("Removal of =",list1.remove((1, 32)))
print(list1)

print("\n\n\n\n")

#When duplicate substring(element) is found
l = [1,2, 4, 3, 6, 3, 7]
print(l)
print("Removal Of first occurrence of matches substring : ", l.remove(3))
print(l)




