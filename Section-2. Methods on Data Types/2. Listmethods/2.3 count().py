'''
    # Syntax : list.count(element)
    # count() does take single parameter
    # Searches for the element in list and returns the number
      of the occurrence of the element
    # If searches element is not found it returns 0
'''

#works with count()
# returns the number of occurrence for the substring(element)
list1 = [1, 4, 5.50, 4, "JK" "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25}]
print(list1)
print("Occurence of {32, 25} : ", list1.count({32, 25}))
print(list1)
print("Occurence of (JK) : ",list1.count("JK"))
print(list1)
print("Occurence of (1,32) : ",list1.count((1, 32)))
print(list1)

print("\n\n\n\n")

#When duplicate substring(element) is found
l = [1,2, 4, 3, 6, 3, 7, 3, 3, 3 ,6]
print(l)
print("Occurence of 3 : ", l.count(3))
print(l)

#when pass the element not in the list
#returns 0 by default
print("Occurence of ggaff : ", l.count("ggaff"))
print(l)



