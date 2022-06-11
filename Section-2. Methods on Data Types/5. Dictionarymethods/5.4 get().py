'''
    # Syntax : dict.get(key, default = None)
    # get() does take two parameters.
    # it returns the value for key, if key exist in dictionary, otherwise returns 
    # 'default' which is 'None'
    # 'default' parameter can be settable or updatable

'''

# works with get()
dict4 = {(1, 5.5, "a", "py") :("Int", "float", "char", "string"), 1 :[1, 2]}
print(dict4)
# getting the key value exist in dict without passing the default
r = dict4.get(1)
print(r)
# getting the key value exist in dict passing the default
person = {'name':'Jaber', 'age':23, 'sex': 'male'}
r = person.get('salary', "Not Avaiable") # setting a default = 'Not Available' 
print(r) # returns the value for that particular key though key exists in dict4

# getting the key value doesn't exist in dict without default passing
# it returns the default parameter, as say default = None
r = person.get("i am awsome")
print(r) # return 'None' though doesn't exist in dict4

# getting the key value doesn't exist in dict with passing the default
# it returns ur new settable default value
r = person.get("ass", "dumb ass!!")
print(r)

