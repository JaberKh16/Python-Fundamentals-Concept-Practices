'''
    # Syntax : set.issubset(other_set)
    # issubset() does take a single parameter
    # Returns True, if all elements of a set are present in another set
    # here, subset means contains all items in another set
    # Mathematically, say two sets are

                 A={2, 3, 4, 9}
                 B={2, 3, 4, 9}
        then,   A < B  ; (<) used for defining as subset sign
        here,  A, B does have all items so they are subset
               sets or vice-versa
    # when no parameter is being passed it gives a TypeError

'''

#works with issubset()
A = {1, 2, 4}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print("A =", A)
print("B =", B)
print("C =", C)

# now comparing with issubset()
r = A.issubset(B)
print(r)
r = B.issubset(A)
print(r)
r = A.issubset(C)
print(r)
r = B.issubset(C)
print(r)
r = C.issubset(A)
print(r)
r =C.issubset(B)
print(r)

# when no parameter is being passed
# it gives a TypeError : issubset() take exactly one argument
r =C.issubset()
print(r)