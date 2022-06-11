'''
    # Syntax : set.pop()
    # pop() doesn't take any parameter
    # Removes an arbitrary(random) element from the set and
      returns the element which is being removed
    # If the set is empty set e.g
              set = {}
              set.pop()
        it raises an error called TypeError

'''

#works with pop()
A = {1, 32, "a", "JK"}
print(A)
#it returns a arbitrary removed item
r = A.pop()
print("Removed item is :", r)

print("\n\n\n")

#when set is empty set
A = {}
r =A.pop()
print("Raise an erro because of Empty Set {} :",r)
