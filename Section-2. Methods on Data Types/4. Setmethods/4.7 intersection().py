'''
    # Syntax : set.intersection(set1, set2, ....)
    # intersection() does take many parameters(sets)
    # Returns a common items in both set
    # Mathematically, say three sets are

                 A={1, 2, 3, 4}
                 B={2, 3, 4, 9}
                 C ={2, 4, 9, 10}
        here, (^) used to referring it intersection sign
        then,  A^B =B^A ={2, 3, 4}
               A^C =C^A ={2, 4}
               A^B^C = {2, 4}

    # when no parameter is being passed it gives a shallow copy of
      the set which is calling the intersection()
          e.g     r = A.intersection()

           returns a copy of set A

    # using (&) operator we can also find the intersection of sets


'''

#works with intersection()
A ={2, 3, 4, 5}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}
print("A =", A)
print("B =", B)
print("C =", C)
r = A.intersection(B)
print("A ^ B = ",r)
r = B.intersection(A)
print("B ^ A =", r)
r =A.intersection(C)
print("A ^ C = ", r)
r =C.intersection(A)
print("C ^ A =", r)
r =A.intersection(B, C)
print("A ^ B ^ C = ", r)
r = B.intersection(A, C)
print("B ^ A ^ C =", r)

#when no parameter is being passed
# it returns a shallow copy of the setA
A ={1, 3, 4}
B ={ 1, 23, 3}
print("A =", A)
print("B =", B)
r = A.intersection()
print(r)


# using (&) operator doing intersection of sets
A ={1, 3, 2, 4, 5}
B = {1, 3, 6, 7}
print("A = ", A)
print("B = ", B)
r = A&B
print("A ^ B =",r)
r = B&A
print("B ^ A =", r)
