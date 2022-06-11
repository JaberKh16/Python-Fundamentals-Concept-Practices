'''
    # Syntax : set.intersection_update(set1,set2,..)
    # intersection_update() does take many parameters(sets)
    # Returns only common items in both set and other items will be
      removed
    # Checks for the intersection() of two sets calling
      intersection_update() and remove the item that is not exist
      in other sets
    # Mathematically, say three sets are

                 A={1, 2, 3, 4}
                 B={2, 3, 4, 9}
                 C ={2, 4, 9, 10}
        here, (^) used to referring it intersection sign
        then,  A^B =B^A ={2, 3, 4}
               A^C =C^A ={2, 4}
               A^B^C = {2, 4}

    # In the Console,
      suppose, r =A.difference_update(B, C)
                   1. r will be None
                   2. A will be equal to the A ^ B ^C
                   3. B will be unchanged
                   4. C will be unchanged
    # when no parameter is being passed it returns None
      because intersection_update() doesn't return any value e.g None



'''

#works with intersection_update()
x = { "Apple", "Banana", "Cherry", 3}
y = {"Google", "Microsoft", "Apple"}
z = {"windows", "macOS", "Linux", "Google", "Apple"}
print("x =", x)
print("y =", y)
print("z =", z )
#retuns value is None
r = x.intersection_update(y, z)
print("Return Value= ",r)
# x set gives the intersection
print("x =", x)
# both y and z set remain unchanged
print("y =", y)
print("z =",z)

#when no parameter is being passed
r = x.intersection_update()
print(r)