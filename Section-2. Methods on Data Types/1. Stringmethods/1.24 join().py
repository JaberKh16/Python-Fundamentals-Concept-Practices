"""
    String Method: join()
    =====================
    # Syntax : str.join(iterable)
    # join() does take a single parameter which is any iterable.
    # iterable's are those which can be iterated though loops such
    as (string, list, tuple, set, dict)
    # Returns a string concatenated with the content of the iterable
    # If the iterable contain non string values, it raises an
      TypeError exception
"""
print("================================================================")

# working of join() with String data_type
s1 = "abc"
s2 = "123"
print("First with s1.join(s2) :\n", s1.join(s2))
print("Second with s2.join(s1) :\n", s2.join(s1))


print("================================================================")
# working of join() with List data_type
numlist = ["1", "w", "3", "4", "JK"]
print(numlist)
separator = ";"
print("join() method with List:", separator.join(numlist))


print("================================================================")
# working of join() with Tuple data_type
numtuple = ("1", "2", "a", "Jk")
print(numtuple)
sep = "-->"
print("join() method with Tuple:", sep.join(numtuple))


print("================================================================")
# working of join() with Set data_type
numset = {"1", "21", "e", "ayesha"}
print(numset)
sep1 = "@@@@"
print("join() method with Sets:", sep1.join(numset))


print("================================================================")
# working of join with Dictionary data_type
# note: if just dictonary name is being passed with join() then its keyword will get joined.
numdict = { "lang " : "Python", "lang2" : "Java", "Int" : 1}
print(numdict)
sep2 = "->->->"
print("join() methods with Dictionary:", sep2.join(numdict))


print("================================================================")
# join() method with the non-string type value
# when dict key isn't the string_type
# it raises the same TypeError with other iterable's
numdict = { 1 : "Python", 2 : "Java", 2 : 1} # raises an TypeError
print(numdict)
sep2 = "->->->"
print("join() methods with Dictionary :\n\n", sep2.join(numdict))

print("================================================================")