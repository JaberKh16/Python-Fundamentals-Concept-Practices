'''
    # Syntax : set.issuperset(other_set)
    # issuperset() does take a single parameter
    # Returns True, if all elements of a set has every element of
      another set(other_set)
    # here, superset means contains all items of another set
    # Mathematically, say two sets are

                 A={2, 3, 4, 9, 10}
                 B={2, 3, 4, 9}
        then,   A U B  ; (U) used for defining as superset sign
        here,  B does have all items of B so A is the superset of B
               and B is the subset of A
    # when no parameter is being passed it gives a TypeError

'''

#works with issuperset()
A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4 }
C = {1, 2, 3, 4 }
print("A =", A)
print("B =", B)
print("C =", C)

# now comparing with issuperset()
r = A.issuperset(B)
print(r)
r = B.issuperset(A)
print(r)
r = A.issuperset(C)
print(r)
r = B.issuperset(C)
print(r)
r = C.issuperset(A)
print(r)
r =C.issuperset(B)
print(r)

# when no parameter is being passed
# it gives a TypeError : issubset() take exactly one argument
r =C.issuperset()
print(r)