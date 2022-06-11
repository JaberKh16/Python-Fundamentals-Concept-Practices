'''
    Nested For Loop Concept
    =======================
    # Syntax : for var_name in iterable:
                    for var_name in iterable:
                        statement1
                        statement2
    # Some iterables are - list, rangem tuple, string, dictionary etc.
    
'''

# works with nested for loop
for x in range(1, 5):
    print("Group :", x)
    for y in range(101, 103):
        print("Members :", y)