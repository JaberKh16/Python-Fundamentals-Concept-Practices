'''
    # Syntax : set.isdisjoint(other_set)
    # isdisjoint() does take a single parameter
    # Returns True, if two sets are disjoint
    # here, disjoint means doesn't have common items
    # Mathematically, say two sets are

                 A={10, 23, 34, 41}
                 B={2, 3, 4, 9}
        here,  A, B doesn't have common items so they are disjoint
               sets

    # isdisjoint() takes an iterable as a parameter
    # it automatically, converts the iterable to set and then checks
      whether the sets are disjoint or not
    # when comparing with iterable (dict_type) set takes dict key's
      as a item and then compare
    # when no parameter is being passed it gives a TypeError

'''

#works with isdisjoint()
A = {1, 2, 3}
B = {5, 6, 7}
C = {4, 5, 6}
print("A = ", A)
print("B = ", B)
r = A.isdisjoint(B)
print(r)

r =B.isdisjoint(C)
print(r)

#When isdisjoint() takes iterable as an arguments
A = {"a", "b", "c", "d", 5}
B = ["b", "e", "f"]
C = "5de4"
D = {1 :"a", 2 : "b"}
E = {"a" :1, "b": 2}
print("Set_type A =", A)
print("List_type B =", B)
print("String_type C =", C)
print("Dict_type D =", D)
print("Dict_type E =", E)

#now checks for disjoint
r = A.isdisjoint(B)
print("Set_type with List_type :", r)
r = A.isdisjoint(C)
print("Set_type with String_type :", r)
r = A.isdisjoint(D)
print("Set_type with Dict_type(D) :", r)
r = A.isdisjoint(E)
print("Set_type with Dict_type(E) :", r)


#when no parameter is being passed
#it gives a TypeError :isdisjoint() takes exactly one argument
r =A.isdisjoint()
print(r)

