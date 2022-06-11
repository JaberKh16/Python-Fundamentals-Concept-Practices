'''
    # Syntax : list.reverse()
    # remove() doesn't take any parameter
    # It reverse the element of a given list
    # It doesn't return any value , returns None

'''

#works with reverse()
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25}]
print(list1)
print("Reverse of List  = ", list1.reverse())
print(list1)

print("\n\n")

#Reverse a list with list[::-1]
l = [1,2, 4, 3, 6, 3, 7]
print(l)
print("Reverse of list: \n")
r = l[::-1]
print(r)




