'''
    # Syntax : set.difference(other_set)
    # difference() does take a single parameter
    # Checks for the difference of two sets
    # difference means say , set1-set2, now returns which items
      are not exist in set1
    # Mathematically, say two sets are--

                  A ={1, 2, 3, 4}
                  B ={2, 3, 9}
        now, if A-B = {1, 4}
             if B-A = {9}
    # It doesnt modify the original sets
    # difference of set can be do with (-) operator


'''

#works with difference()
A = {"a", "b", "c", "d", 1}
print(A)
B = {"c", "g", "f", 3}
print(B)
#now A-B
r =A.difference(B)
print(r)
#now B-A
r =B.difference(A)
print(r)

#with (-) operator
A = {1, 2,43, "a"}
B = {"a", 24, 2, 1}
r = A-B
print(r)
r = B-A
print(r)