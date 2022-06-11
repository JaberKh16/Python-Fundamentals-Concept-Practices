'''
    # Syntax : dict.update(iterable[key, value])
    # update() does take a single parameter
    # it updates the dict with the element from another dict object
      or from an iterable of (key/value) pairs
    # it adds if the key isn't exist in dictionary already
    # And if the key is exist in dict , it can be updatable with new value
    # generally it pop form the last key's from dict as so forth
    # If the update() is passed without parameters , the dict remains
      unchanged
    # it doesn't return any  value e.g None

'''

# works with update()
dict1 = {1 :[1, 3], "JK": "Ayesha", 3 :5.5}
print(dict1)

# now using update() with parameter
dict1 = {1 :[1, 3], "JK": "Ayesha", 3 :5.5}
dict2 = {2 : "two"}
r = dict1.update(dict2)
print("Return value is :", r)
# displaying the dict1
print(dict1)
print(dict2)

# update() with iterable(generally tuple)
p = { "x" :2}
# when same key isn't being passed
p.update(y = 3, z =4)
print(p)

# when passing the same key with new value
# it updates the value of that key exist
p.update(y = 3, x =4)
print(p)