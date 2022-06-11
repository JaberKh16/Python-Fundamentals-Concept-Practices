'''
    # Syntax : dict.values()
    # values() doesn't take any parameter
    # it returns a view object that displays a list of dict(values) as
      like list in items


'''

#works with values()
dict1 = {1 :[1, 3], "JK" : "Ayesha", 3 :5.6}
print(dict1)

# now using values()
r = dict1.values()
print("List_type items from dict_type(values) :", r)
