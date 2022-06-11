'''
    # Syntax : set.difference_update(other_set)
    # difference_update() does take a single parameter
    # Checks for the difference of two sets calling difference_update()
    # difference means say , set1-set2, now returns which items
      doesn't exist in set1
    # Mathematically, say two sets are--

                  A ={1, 2, 3, 4}
                  B ={2, 3, 9}
        now, if A-B = {1, 4}
             if B-A = {9}
    # In the Console,
      suppose, r =A.difference_update(B)
                   1. r will be None
                   2. A will be equal to A-B
                   3. B will be unchanged
    # It doesnt modify the original sets
    # it doesn't return any value e.g None

'''

A = {"a", "c", "g", "d"}
B = {"c", "f", "g"}
r =A.difference_update(B)
# A returns which items doesn't exist in B
print("A =", A)
#B remains unchanged
print("B =", B)
#it returns None
print("Result =", r)

