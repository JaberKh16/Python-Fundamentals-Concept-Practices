'''
    # Syntax : dict.fromkeys(sequence(keys)[, value])
    # fromkeys() does take two parameters
    # Creates a new dict from the given sequence of element with a value
      provided by the user
    # Now about parameters,
        1. Sequence of elements which is to be used as 'Keys' for the new dict
        2. Value which is set to each each element of the dict
    # Sequence(keys) can be any iterable(string, set, tuple)
    # Value can be settable .
    # By default value is 'None' .


'''

# works with fromkeys()
# creating keys as Set(iterable)
keys  = {"a", "e", "i", "o", "u"}
print("Sequence of element(Set_type)",keys)

# now using fromkeys() method
# it creates a new dict with keys provides and the values will be set as 'None'
r = dict.fromkeys(keys)
print("New dict from set_type(keys) is :", r)
# check for the keys
print(keys)

# nows creating keys as Tuple(iterable)
keys = (1, 3, "a")
r = dict.fromkeys(keys)
print("New dict from tuple_type(keys) is :", r)
print(keys)

# now creating keys as String(iterable)
keys = "Password"
r = dict.fromkeys(keys)
print("New dict from string_type(keys) is :", r)
print(keys)

# When passing two parameters (sequence , value)
# now with a string_type
keys = "pass"
value = 1213
r = dict.fromkeys(keys, value)
print(value)
print(keys)
print("New dict with value paramter :", r)

# now with a mutable object list
keys = {"a", "e", "i", "o", "u"}
values = [1]
r = dict.fromkeys(keys, values)
print(values)
print(keys)
print("New dict with value paramter :", r)


# now with a mutable object list
# while we updating the mutable list the value of new dict is
## also get updated, that because we give the reference of mutable object
keys = {"a", "e", "i", "o", "u"}
values = [1]
values = values.append(2) # update the values list
r = dict.fromkeys(keys, values)
print(values)
print(keys)
print("The value get updated In new dict item because of mutable reference passed")
print("New dict with value paramter :", r)


# now to avoid mutable object issue

# here, r ={Key : list(v) for Key in keys}
##here Key is the object we made by own explicitly
## it can be also done like this as follows--->
## r = { Key : value[:] for Key in keys}

keys = {"Jaber", "Karim", "Sakib", "Ajhar", "Renu"}
values =['C++', 'Java', 'Python']

new_dict  = {Key :list(values) for Key in keys}
print("Dictionary \'r\' = ",new_dict)
print("Mutable Object is :",values)
print("Sequence(Keys) is ",keys)
print("New dict is :",new_dict)



