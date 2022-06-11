"""
[To Cleear The Dictionary Data --> use dict.clear() method]

    # Syntax : dict.clear()
    # clear() doesn't take any parameter.
    # It Clears all th element from the dictionary
    # It doesn't returns any value e.g None
"""

# works with clear()
dict1 = {53 : "HTTP", 23 :"Telnet", 55 :"SSH", "a" : "JK"}
print(dict1)

# now clearing the dict1 using dict.clear() method
r = dict1.clear()
# it returns None
print(r)

# showing the cleared dict1
print("After using clear() :", dict1)



