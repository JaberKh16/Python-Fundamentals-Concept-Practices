'''
    # Syntax : dict.keys()
    # keys() doesn't take any parameter
    # it returns a view object that displays a list of dict(keys) as
      like list in items


'''

#works with keys()
dict1 = {1 :[1, 3], "JK" : "Ayesha", 3 :5.6, 'a':12}
print(dict1)

# now using keys()
check_keys = dict1.keys()
print("List_type items from dict_type(keys) :", check_keys)

print(type(check_keys)) # checking its type

# can also looping over the dict_keys([]) though its containg a list 
for keys in dict1.keys():
  print(keys) 