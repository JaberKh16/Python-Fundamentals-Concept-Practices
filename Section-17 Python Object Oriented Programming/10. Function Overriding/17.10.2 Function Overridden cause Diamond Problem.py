"""
 This Program will demonstrate about the Diamond Problem in Inherihentacne.
 here , i will use the diamond class pattern as like -->   A <-- B --< C --< D(A, C)

"""


class A:
    def message(self):
        print('I am from the class A')

class B(A):
    def message(self):
        print('I am from the class B')

class C(B):
    def message(self):
        print('I am from the class C')

class D(C, A):
    pass

# creating the class instance 
d = D()
d.message() # this will hit the class C 'message()' why because of MRO

