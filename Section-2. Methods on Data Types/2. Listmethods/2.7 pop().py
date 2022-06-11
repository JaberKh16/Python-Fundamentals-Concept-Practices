'''
    # Syntax : list.pop(index)
    # pop() does take a single parameter
    # Searches for the element in list and removes
      the first matching substring(index) of that index
    # If duplicate elements are present in list it removes the
      first occurrence of the matches substring index
    # When no parameter is passed the default value is -1
      which returns the last value of the list
    # If searches element is not found is raises a ValueError exception
'''

#works with pop()
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25}]
print(list1)
print("Return Value  = ", list1.pop(8))
print(list1)
print("Return Value  = ",list1.pop(3))
print(list1)
print("Return Value  = ",list1.pop(2))
print(list1)

print("\n\n\n\n")

#When wrong index is passed
l = [1,2, 4, 3, 6, 3, 7]
print(l)
print("Return Value  =  : ", l.pop(0))
print(l)

#when -1 is passed
lan = ["Python", "Java", "C", "JavaScript", "Ruby", "C++", "PHP"]
print(lan)
print("Return Value  = ", lan.pop(-1))
print("Updated List :", lan)

print("Return Value  = ", lan.pop(-3))
print("Updated List :", lan)

#when no parameter is passed
# it takes the by default value -1
# returns at -1 index
l =["Python", "Java", "PHP", "C++"]
print(l)
r = l.pop()
print("Return Value :", r)
print("Updated List :", l)



