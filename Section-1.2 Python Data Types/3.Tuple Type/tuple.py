'''
   # Python Tuple DataType
   =========================
   # Tuple is a sequence of immutable items.
   # Tuple is Immutable means can't changeable.
   # It is defined by value separated with comma's inside parenthesis()
   # Tuple items can be access via Indexing.
   # Any operation with operands is possible with Tuple DataType
   # Tuple can hold any kind of object such as iterables(string, list, set) and even Primary Datatypes.
'''
# declaring a tuple
tuple1 = (1, 3, 5, "Ayesha", "JK", "a", [1, 2, 5.0, "a"], 7.50, "c")
print(tuple1)

# tuple can take other iterables like ---> (list, tuple, set, dictionary)
tuple2 = (4, 24.4, ("a", "Eat"), {4.5, 4}, {1:"Python"})
print(tuple2)

# access value of tuple via indexing 
tuple1[0]
print(tuple1[0])
print(tuple1[3])
print(tuple1[6][3])

# slicing the tuple
print(tuple1[0:5])
print(tuple1[:-1])
print(tuple1[:-2])
print(tuple1[-3:-1])

# checking the length of the tuple
print(len(tuple1))

# repitition the value of tuple
print(tuple1*2)


# concatenating the previous tuple1 with tuple2
tuple2 = (4, 24.4, ("a", "Eat"), {4.5, 4}, {1:"Python"})
print(tuple2)
print(tuple1 + tuple2) # concatenation via '+' operator

# concatenate via indexing with tuple
tuple3 = [ "Python", "C++", "Java", ("Love", 4)]
tuple4 = (1, 2)
print(tuple4)
print(tuple4[1]+tuple3[3][1])

# concatenate via slicing with tuple
tuple3 = ( "Python", "C++", "Java", ("Love", 4))
tuple5 = (1, 2, "JK")
print(tuple3)
print(tuple3[-3:-1] + tuple5[:-1])
print(tuple3[-3:] + tuple5[:-1])


# checking immutability via assigning value
tuple5 = (1, 2, 4)
tuple5[3] = 12 # TypeError: 'tuple' object does not support item assignment
print(tuple5) 
