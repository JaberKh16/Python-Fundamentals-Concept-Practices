'''
    next() Method On Iterating String Type
    ======================================
    #   String Datatype is an iterables not an iterator.
    #   To iterate with next() method throws an exception 
        saying - TypeError: 'str' object is not an iterator

'''

def generator_function():
    string_value = "Yasoooq"
    x = next(string_value) # trying to iterate string type hits an exception
    print(x)

print(generator_function())
