'''
    # Syntax : list.insert(index,element)
    # insert() does take a two parameters
    # Insert specified element at the specified index
    # insert() doesn't return anything, instead returns None. Only updates the current list.
    # If searches element is not found is raises a ValueError exception
'''

# works with insert()
list1 = [1, 4, 5.50, "JK", [2, 5, "a"], "Ayesha", "c", (1, 32), {32, 25}]
print(list1)
print("Insert at index-2. = ", list1.insert(2, 25))
print(list1)
print("Insert at index-5. =",list1.index(5,"JK"))
print(list1)


# passes tuple as a parameter called element
list1 = ["cat", "dog", "horse", {1, 32}, [3, 5]]
number_tuple = ( 35 , 5.34)
print("Passed tuples as an element \n")
list1.insert( 1, number_tuple)
print("Tuple elements are: ", number_tuple)
print("After insertion: ", list1)




