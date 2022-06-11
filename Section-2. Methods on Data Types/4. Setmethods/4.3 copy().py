'''
    # Syntax : set.copy(element)
    # copy() doesn't take any parameter
    # Returns a shallow copy of the set
    # It doesnt return any value e.g None


'''

#works with copy()
n = {1, 3, 4.5, "a"}
print(n)
p = n.copy()
print(p)

# A set can be copied using assignment (=) operator
n = {1, 2,42}
p =n
print(n)
print(p)

#updating a set item also modified the other variable which copied the set
n.add("s")
print(n)
print(p)
