"""
    String Method: rpartition()
    ===========================
    # Syntax : str.rpartition(separator)
    # rpartition() does take a single parameter which is need to be provided.
    # Returns a 3-tuple data_type of given string data_type
    # It splits the string at the first occurrence of the substring
    (separator) string and returns a tuple.
    # And it just a right_justified partition technique.
    # When no argument is passed it gives a 'ValueError' exception'

"""

print("==============================================================")
# working with partition()
s = "python"
print(s)
print("Now After Partitioned the given string:")
print(s.rpartition("python")) # returns 3-tuple data_type
print("==============================================================")

# working with partition()
# returns e.g --->    ( ' ' , ' ' , 'given str'  )  # 3-tuple data_type
s = "Python is  fun"
print(s)
print(" Now After Partitioned the given string : \n\n")
print(s.rpartition("is"))
print(s.rpartition("is fun"))
print(s.rpartition("Python is fun"))
print(s.rpartition("fun"))
print(s.rpartition("Python"))


print("==============================================================")
# when (wrong subrting separator is being passed) as a argument
# returns e.g --->  (  '' , '',  'given str'  )  # 3-tuple data_type
r = " i dont know"
print(r)
print(r.rpartition("asdfd"))


print("==============================================================")
# when working with empty string
# returns e.g --->    (  ' ',  ' ', 'str'  )
r = ""
print(r)
print(r.rpartition("wfgw"))
print(r.rpartition("")) # it raises an ValueError: empty separator

print("==============================================================")