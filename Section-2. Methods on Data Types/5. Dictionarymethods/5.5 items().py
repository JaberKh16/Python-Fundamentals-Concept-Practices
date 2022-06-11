'''
    # Syntax : dict.items()
    # items() doesn't take any parameter
    # it returns a view of object that displays a list of dictionary's
      (key/value) as tuple pair

'''

#works with items()
p = { 1: "S", "JK" : "Ayesha", 2 :[1, 3]}
print(p)

#now using items()
#it returns a dict (key/value) as tuple data_type
r = p.items()
print("Tuple Pair of dict_type :", r)
