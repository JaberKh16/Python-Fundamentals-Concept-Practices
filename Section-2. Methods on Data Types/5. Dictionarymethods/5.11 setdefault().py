'''
    # Syntax : dict.setdefault(key[, default_value])
    # setdefault() does take two parameters
    # it returns the value of the key(if exist) passed as argument
      or else it inserts a key with a value to the dict
    # if wrong key is being passed it gives the default_value
    # And if the key is exist in dict ,then it inserts a defaut_value to
      the dict
    # default_value can be settable
    # default_value is by default None


'''

# works with setdefault()
p = {"name" :"Jhon", "age" : 23}
print(p)

# now using setdefault() exist key in dict
# it returns the key value
a = p.setdefault("age") # setting the key:age as default
print("Return Value is :", a)

a2 = p.setdefault("name")
print("Return Value is :", a2) # setting the key:name as default

# when key isn't in dict with no default_value
p = {"name" : "Jhon"}
s = p.setdefault("a")
print("Return value is :", s)

# setting a default_value
p = {"name" : "Jhon"}
r = p.setdefault("a", 2)
print("After setting the default_value :", r)



