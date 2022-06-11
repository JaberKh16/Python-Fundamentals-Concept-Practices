"""
    String Method: partition()
    ==========================
    # Syntax : str.partition(separator)
    # partition() does take a single parameter which is need to be provided.
    # Returns a 3-tuple data_type of given string data_type
    # It splits the string at the first occurrence of the substring
    (separator) string and returns a tuple.
    # And it a middle_justified partition
    # When no argument is passed it gives a 'ValueError' exception.

"""

print("=============================================================")
# working with partition()
s = "python"
print(s)
print("Now After Partitioned the given string:")
print(s.partition("python")) # returns 3-tuple data_type


print("=============================================================")
# working with partition()
# returns e.g --->    ( ' ' , 'given str' , ' '  )  # 3-tuple data_type
s = "Python is  fun"
print(s)
print("Now After Partitioned the given string:")
print(s.partition("is"))
print(s.partition("is fun"))
print(s.partition("Python is fun"))
print(s.partition("fun"))
print(s.partition("Python"))



print("=============================================================")
# when (wrong substring separator is being passed) as a argument
# returns e.g --->  ( 'given str' , '' , ''  )  # 3-tuple data_type
r = "i dont know"
print(r)
print(r.partition("asdfd"))



print("=============================================================")
# when working with empty string
# returns e.g --->    (  ' ',  'str', ' '  )
r = ""
print(r)
print(r.rpartition("wfgw"))
print(r.rpartition("")) # it raises an ValueError: empty separator

print("=============================================================")