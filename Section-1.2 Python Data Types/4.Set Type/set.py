'''
  # Python Set Datatype
  ======================
  # Set is a unordered and unindexed collection  of unique items.
  # It is defined by value separated with comma's inside braces {}
  # Set can't be access via Indexing, means no index operation on Set.
  # Any operation with operands is not possible with "Set DataType"
  # Set items can't be changeable.
  # Sets can only take iterables (string and tuple)
  # Set can't take a item which is Set DataType, it gives an exception saying,
          TypeError : unhashable type: 'set'
    Means , Set can't hold a similar(homogeneous) DataType.
  
  Note: Not a good practice to declare an empty string with {} then it will
        be considered as an empty dictionary.

'''

# Declaring an String Object and then assign the object to the set()
p = "Welcome to Python "
x = set(p) # creating a set using the set(object) function
print(x)

p = "I am awsome and i dont know"
x = set(p) # creating a set using the set(object) function
print(x)

# Access the Set Elements via looping
set1 = {"apple", "banana", "Cheery", "a", 213}
print(set1)
for x in set1:
  print(x)

# With "in" keywords checking if an element is in set1
# returns True if element is in set1
print("apple" in set1) # chekcing does the set1 variable contains "apple" value 
print("adfdaf" in set1) # checking does the set1 variable contains "adfdaf" values

# To check any element isn't in Set use "not" keyword
# returns True if the element is not in the Set.
print("afe" not in set1) # checks set1 doesn't  contains "afe" value
print("apple" not in set1)



# creating an empty set with {} only leads to empty dictionary
empty_set = {}
print(type(empty_set))

# Creating Set using {} notation
# which gives an TypeError : unhashable type : 'set'
q = {"apple", 1, 5.34, {1, 3}, "a"} # Set is holding a Set DataType which is cause an exception
print(q)
