'''
    # Syntax : set.update(element)
    # update() does take many parameters (sets)
    # It adds element to the set which is calling the update()
    # As a (element)Parameter, it takes iterable(string, list, tuple, dict,set)
      automatically converted iterable to set and then update

    # It doesn't return any value e.g None

'''

#works with update()
A = {"a", "b"}
B = {1, 2, 3}
print("A =", A)
print("B =", B)
r = A.update(B)
#set A is updated
print("A =", A)
#set B remains unchanged
print("B =", B)
#returns value is None
print("Return Value :", r)

# work with other iterable

#work with string
str1 = "abc"
set1 = {1, 3}
print("String :",str1)
print("Set :",set1)
r =set1.update(str1)
#set1 is being updated
print("Set :",set1)
#str1 remains unchanged
print("String :",str1)
#return value is None
print("Return Value :", r)

#work with dictionary
str1 = "abc"
dict1 = { "key" : 1, "eat" : 2, 2:"lock"}
set1 = {1, 3}
print("String :",str1)
print("Dictionary :",dict1)
print("Set :",set1)
r =set1.update(str1, dict1)
#set1 is being updated
print("Set :",set1)
#str1 remains unchanged
print("String :",str1)
#str1 remains unchanged
print("Dictionary :",dict1)
#return value is None
print("Return Value :", r)


