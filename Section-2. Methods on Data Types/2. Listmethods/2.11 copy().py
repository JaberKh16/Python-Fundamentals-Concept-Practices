'''
    # Syntax : list.copy()
    # copy() does take a single parameter
    # Returns a shallow copy of the list

'''

#work with copy()
list1 =[1, 33, 5.345, "a", ["Ayesha", "a", 5], 4.5]
print(list1)
list2 = list1.copy()
print(list1)
print(list2)
list2.append("Khan")
print(list1)
print(list2)
list1.append("a")
print(list1)
print(list2)

# copy list with assignment operator
list1 =[1, 3, 4,"q"]
print(list1)
list2 = list1
print(list2)
list1.append("a")
print(list1)
print(list2)
list2.append("v")
print(list1)
print(list2)
del list2[5]
print(list2)
print(list1)
del list1[4]
print(list1)
print(list2)

