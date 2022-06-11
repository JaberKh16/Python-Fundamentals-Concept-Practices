'''
      Iterable- range() Function Concept
      ==================================
      Syntax : range(start, stop, [step])

      # range is versatile function which creates a iterable yielding
        arithmetic progression.
      # range() creates a object of that is range if simply being called.
      # range() function can used other data_typess such as- 
        list, tuple, set, dictionary.

'''

# range(n) creates a object of range function
x = range(5) # n=5
print(x)
x = range(0, 10, 1) # start = 0, stop=10, increment=1
print(x)


# range() function works with other data_type(list)
n = list(range(0, 10, 1))
print(n)

#range() function works with other data_type(tuple)
n = tuple(range(0, 10, 1))
print(n)

# range() function works with other data_type(set)
n = set(range(0, 10, 1))
print(n)

# range() function works with other data_type(string)
# it returns the range object
n = str(range(0, 10, 1))
print(n)

# range() function works with for loop
for x in range(1, 10, 1):
    print(x) # prints 1 to 10

