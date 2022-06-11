'''
    # Syntax : list.append()
    # append() does take a single parameter
    # Returns a list with added item in the last in the items of
      the existing list
'''

#works with append(item)
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", [1, 32]]
print(list1)
print(list1.append("a"))
print(list1)
print(list1.append(7))
print(list1.append("h"))
print(list1)

#Adding list to list
list1 = ["cat", "dog", "horse"]
list2 = ["meaaaaw", "Ruff", "SHHHHHHH", 1, "a"]
print("list1 append with list2 \n")
r = list1.append(list2)
print(list1)

print("list2 append with list1 \n")
r = list2.append(list1)
print(r)   #Returns None

#Tuple can't append with list
#returns None
tuple1 =(1,23, "a", "JK")
print(tuple1)
r =list1.append(tuple1)
print(r)
