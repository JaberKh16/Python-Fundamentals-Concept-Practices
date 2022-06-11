'''
    # Syntax : list.extend(list1)
    # extend() does take a single parameter
    # Returns a extended list with added list in the end of the items of
      the existing list
    # it doesn't return any value
'''

#works with extend(iterable)
#Returns None when single string is beimg passed because of str(chr)
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", [1, 32]]
print(list1)
print(list1.extend("a"))
print(list1)
#Breaks at every character make
print(list1.extend("hada"))
print(list1)

#Adding list to list
list1 = ["cat", "dog", "horse"]
list2 = ["meaaaaw", "Ruff", "SHHHHHHH", 1, "a"]
print("list1 append with list2 \n")
list1.extend(list2)
print(list1)

print("list2 append with list1 \n")
list2.extend(list1)
print(list2)   #Returns None

#extend tuple_type to list
list1 =[1, 3, "a", ["Ayesha", "JK"], 5.0]
print(list1)
tuple1 = (1, 3, "a")
print(tuple1)
list1.extend(tuple1)
print(list1)

#extend set_type to list
set1 = {1, 3, "c"}
print(set1)
list1.extend(set1)
print(list1)

#extend list via assignment (+=/+)
# gives a reference of the other list
a =[1, 3]
b =[3, 23, "a"]
a+b
print("a :", a)
print("b :", b)
a+=b
print("a :", a)
print("b :", b)

# can do the same with tuple

tuple1 =("Jaber", 23)
tuple2 = ("Ayesha", "Khan")
tuple1+=tuple2
print("Tuple1 :", tuple1)
print("Tuple 2 :", tuple2)


