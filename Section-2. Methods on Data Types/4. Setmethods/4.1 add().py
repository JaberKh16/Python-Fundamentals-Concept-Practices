'''
    # Syntax : set.add(element)
    # add() does take a single parameter
    # It add a given element to the set, if element isn't exist already
    # You cant get the old set while u already use add() methods
      because it doesn't returns a reference to the set but None
      Clearly, add() returns None

'''

#work with add()
q = {"Jk", "a", "123", 5, 6.5}
print(q)
print(q.add("Ayesha")) #returns None
print(q)

#other iterable add to set using add()

# add tuple to a set
q ={1, 5.42, "c", "JK"}
print(q)
tup = ("Ayesha", "Khan", 90, (1, 2))
print(tup)
q.add(tup)
print(q)

#add list to a set
# It gives an error called TypeError :unhashable type :'list'
q = {1, 25, "a", "JK", (113,"a")}
print(q)
c = [1, 342]
print(c)
q.add(c)
print(q)





