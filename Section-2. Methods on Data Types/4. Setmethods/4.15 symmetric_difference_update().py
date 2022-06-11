'''
    # Syntax : set.symmetric_difference_update(other_set)
    # symmetric_difference_update() does take a single parameter
    # Returns a new set which is symmetric difference of two sets
      via calling symmetric_difference
    # Symmetric difference update means,

         say, A and B are two sets. then there symmetric difference is
         elements of either A or B, but not it both
         simply, removes the item that are common in both set and insert
         the item which are not in both sets and make a set
    # It update the original set which is calling by this method
    # It doesn't return any value e.g None
'''

#works with symmetric_difference_update()
A = {"a", "c", "d"}
B = {"c", "d", "e"}
print("A =", A)
print("B =", B)
r = A.symmetric_difference_update(B)
# updates the set A
print("A =", A)
# set B remains unchanged
print("B =", B)
# it doesn't return any value e.g None
print("Return Value is = ", r)