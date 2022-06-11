"""
[To Copy a Dictionary Data --> use dict.copy()]

    # Syntax : dict.copy()
    # copy() doesn't take any parameter
    # it returns a shallow copy of the dictionary
    # using (=)assignment operator u can get the copy of the dict item

"""

# works with copy()
dict1 = {1 : "a", 3: "Derek", "a":"JK", 5.50 :"float"}
print(dict1)

# now copying the dict1 item with copy()
# remember copy() methods a deep copy
r = dict1.copy()
print("New dict2", r)

# using assignment (=) operator copying the dict1
# copying dict1 to dict2 using = , actually gives the reference of
## dict1 to dict2 , so when you modified dict1/dict2 it also get updated
dict1 = {"a":1, 2 :"SSH", 3 :"HTML"}
dict2 = dict1
print(dict1)
print(dict2)

# updating the dict1 via direct assignment
dict1[32] = "HTTP" 
print(dict1)
print(dict2)


