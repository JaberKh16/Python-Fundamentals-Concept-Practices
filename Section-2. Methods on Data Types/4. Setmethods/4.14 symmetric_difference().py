'''
    # Syntax : set.symmetric_difference(other_set)
    # symmetric_difference() does take a single parameter
    # Returns a new set which is symmetric difference of two sets
    # Symmetric difference means,

         say, A and B are two sets. then there symmetric difference is
         elements of either A or B, but not it both
         simply, removes the item that are common in both set and insert
         the item which are not in both sets and make a set
    # In Python, using (^) operator , can also find the
      symmetric difference of two sets

'''

#works with symmetric_difference
A = {"a", "b", "c", "d"}
B = {"c", "d", "e"}
C = {}
#now checks for symmetric_difference()
r = A.symmetric_difference(B)
print(r)

r = B.symmetric_difference(A)
print(r)

r = A.symmetric_difference(C)
print(r)

r = B.symmetric_difference(C)
print(r)

# Using (^) to find the symmetric difference
A = {"a", "b", "c", "d"}
B = {"c", "d", "e"}
print("A =", A)
print("B =",B)
r = A^B
print("Symmetric Difference A^B =", r)
r = A^A
print("Symmetric Difference A^A =", r)
r = B^A
print("Symmetric Difference B^A =", r)
r = B^B
print("Symmetric Difference B^B =", r)