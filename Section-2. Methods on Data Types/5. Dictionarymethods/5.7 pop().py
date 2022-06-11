'''
[To pop item from the dicitonary and gets the popped key value]

    # Syntax : dict.pop(Key[, default])
    # pop() does take any parameter
    # it removes the key passed as a parameter and returns the corresponding
      value of that key
    # If key isn't found in dict, default value is returned
    # if default value is not given it raises an KeyError


'''

# works with pop()
dict7 = {1 :[1, 3], "JK" : "Ayehsa", 3:"a", 5.5 :"f"}
print(dict7)

# now using pop()
r = dict7.pop(1)
print("Returning the Value of passing Key :",r)

# now seeing left item in dict
print(dict7)



# when passing the wrong keys(doesn't exist) in dict and default is set
# it gives the set default value
r = dict7.pop("A", 'doesnt exist')
print(r)


# when passing the wrong keys(doesn't exist) in dict and default isn't set
#r = dict7.pop("A") # it gives an error called KeyError : 'A' , because default value isn't set
# print(r)

# creating a dictionary of fruits containin how many of them are available!
fruits = {'apple':2 , 'banana':3, 'orange':4, 'pineapple':3}

# pop the items from the dictionary via looping
for fruits_item in fruits.keys():
  print(fruits.pop(fruits_item)) # all keys
  
  

    
    
  