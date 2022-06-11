'''
  # Python Dictionary DataType
  =============================
  # Dictionary  is a sequence of  items like key value mapping data structure.
  # It is defined by separated with {key : value}
  # Only difference is that dict_type creates custom indexed by
    itself explicitly which is actually a 'key', means 'key' is the index.
  # Here, key's can be any data_type but not 'List' and 'Set'
      if included it gives TypeError : unhashable type :'set'/'list'

  # Dictionary items can be access via Key .
  # Any operation with operands isn't possible with Dictionart DataType.
  # Slicing is not possible with Dictionary DataType.

'''

# Declaring a Dictionary
dict1 = {1: 3, 5 :"Ayesha", "JK":"a", 7.50 : "c", "c" :"a", "JK" : "Ayesha"}
print(dict1)

# Dictionary can take other iterables like ---> (tuple, set, dictionary)
dict2 = {4 :24.4, 2: ("a" ,"Eat"), "a" :{4.5, 4}, 1 :{"Python"}}
print(dict2)

# Accessing Value of dictionary via it's key value similar like indexing with key's
# If Any Key doesn't exists in the dictionary then it will a "KeyError Exception"
dict1[1]
print(dict1["JK"])
print(dict1[7.50])
print(dict1["c"])

# Access Value of dictionary using get()
# Using get() has a facility if specified key isn't exists in the dictionary
# then it returns "None".
print(dict1.get(1)) # get() will returns the specified key index value


# Length of the list
print(len(dict1))

# Deleting element form the dict via key
p = {22: "SSH", 23 :"Telnet", 53 : "HTTP"}
print("Before deleting :",p)
del p[23] # deleting key "23"
print("After deleting :",p)

#Updating dict  via overridden key with new value

p = {22: "SSH", 23 :"Telnet", 53 : "HTTP", 53 :"SSS", 56:"i m awsome"}
print(p)
# Overriddern with key
# If, a Key is already exist any new value with the same key in Dictionary,
# is overridden the Key Value in the Dictionary
p[23] = "I dont know" # Key = 23 will be overidden with new value 'I dont know'
print(p)

# Adding item to dict with keys
p = {22: "SSH", 23 :"Telnet", 53 : "HTTP", 53 :"SSS", 56:"i m awsome"}
print(p)

# Adding with new key with value
# If, no Key exist already in Dictionary ,then Dictionary can add a new value 
# with the new {Key, Value} pair item. 
p[25] = "Telnet2"
print(p)


# Slicing with Dictionary
# It gives an error called TypeError : unhashable type :'slice'
print(dict1[:-1])




