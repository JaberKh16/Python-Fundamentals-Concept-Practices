'''
    # Syntax : set.union(set1, set2, .....)
    # union() does take many parameters (sets)
    # Returns a union of sets
    # when no argument is passed it returns a shallow copy of set.
         e.g     r = A.union()

        it returns the copy of set which calling the union() method

'''

#works with union()
A = {"a", "b", "c", "d"}
B = {"d", "banana", "macOS", 4}
C = {1, 3, 4}
print("A =", A)
print("B =", B)
print("C =", C)
#set A is being Updated
r =A.union(B)
print(r)
# set B remains unchanged
print("B = ", B)

r = A.union(B, C)
print(r)

print("B = ", B)
print("C =", C)

# when no parameter is being passed
A = {"a", "b", "c", "d"}
B = {"d", "banana", "macOS", 4}
print("A =", A)
print("B =", B)
r = A.union()
print(r)

# when set A is union() by set A
# it also returns the shallow copy of set A
# because of duplicate items is being cleared
A = {"a", "b", "c", "d"}
print("A =", A)
r = A.union(A)
print(r)

