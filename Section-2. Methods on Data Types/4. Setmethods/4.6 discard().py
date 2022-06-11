'''
    # Syntax : set.discard(element)
    # discard() does take a single parameter
    # removes a specified element from the set(if exist)
    # it doesn't return any value

'''

# works with discard()
n = {2, 3, 4, 5 }
print(n)
r = n.discard(3)
#it returns None
print("Return Value =", r)
print("Set Left item are = ", n)
