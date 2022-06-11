'''
   # Python List DataType
   ========================
      
      #  List is a sequence of items. It is a Sequence Type DataType.
      #  List is a mutable type object means it can be changable/modifiable.
      #  It is defined by value separated with comma's inside braces []
      #  List can contains various DataTypes e.g other iterable(strings, tuples) and
         also primary datatypes(such as integer, float, character).
      #  List items can be accessible via Indexing.
      #  List also support Slicing Technique.
      #  Any operation with operands is possible with List DataType
      #  Can also Store other objects in a List -- such as,
      
            1. tables objects(contains lots of data)
      
            2. Files
      
            3. Widges(Graphical User Interface)


'''

# Declaring a List
list1 = [1, 3, 5, "Ayesha", "JK", "a", [1, 2, 5.0, "a"], 7.50, "c"]
print(list1)

# List can take other iterables like ---> (tuple, set, dictionary)
list2 = [(4, 24.4, ("a", "Eat"), {4.5, 4}, {1:"Python"})]
print(list2)

# Access Value of list via indexing with list
list1[0]
print(list1[0])
print(list1[3])
print(list1[6][3])

# Slicing the List
print(list1[0:5])  
print(list1[:-1])
print(list1[:-2])
print(list1[-3:-1])

# Length of the List
print(len(list1))

# Repetation of List
print(list1*2) # 'list1' will be repeated twice 

# Concatenating the previous 'list1' with 'list2'

list2 = [(4, 24.4, ("a", "Eat"), {4.5, 4}, {1:"Python"})]
print(list2)

print(list1 + list2) # concatination of list done via '+' operator

# Concatenate via indexing with List
list3 = [ "Python", "C++", "Java", ("Love", 4)]
list4 = [1, 2]
print(list4)
print(list4[1]+list3[3][1])

# Concatenate via Slicing with List
list3 = [ "Python", "C++", "Java", ("Love", 4)]
list5 = [1, 2, "JK"]
print(list3)
print(list3[-3:-1] + list5[:-1])
print(list3[-3:] + list5[:-1])

