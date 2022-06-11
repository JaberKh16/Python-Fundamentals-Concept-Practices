'''
    # Syntax : dict.popitem()
    # popitem() doesn't take any parameter
    # it removes arbitrary(random) key and returns the corresponding
      (key,value) pairs of tuple_type
    # generally it pop form the last key's from dict as so forth
    # If it's empty dict then it gives an error call ed KeyError
            e.g KeyError :'popitem() : dict is empty'


'''

# works with popitem()
dict1 = {1 :[1, 3], "JK": "Ayesha", 3 :5.5}
print(dict1)

# now using popitem()
r = dict1.popitem()
print("Tuple_type pairs of arbitrary(keys) keys :", r)
# displaying the dict1
print(dict1)

r =dict1.popitem()
print("Tuple_type pairs of arbitrary(keys) keys :", r)
# again displaying the dict1
print(dict1)

