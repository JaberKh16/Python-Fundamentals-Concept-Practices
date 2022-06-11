"""
    # Indexing wtith Python String
    ===============================
    # Indexing on sequence can be possible in Python.
    # In Python, indexing is start with 0.
    # Indexing value only can be integer type.
    
"""

# working with String Data Type
x = "i am awesome"
print(x)
x[0] # this will select the 1st character from the string object 'x'
print(x[0]) # this will print the first index element 'i'
print(x[-1])  # will print the last index element 'e'



# here range in indexing works like upperexclusive means cantprint exceeds
# lower bound is inclusive
# upper bound and cant go bottom then lower index means upper bound is exclusive
# prints between range in index x[2:3] prints the middle of that range value
print(x[2:3])
print(x[-4:-1]) # going backwards to -4 from -1 then included the string in
                # range -4 to -1
