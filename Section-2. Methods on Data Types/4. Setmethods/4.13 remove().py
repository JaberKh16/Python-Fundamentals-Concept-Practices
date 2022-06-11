'''
    # Syntax : set.remove(element)
    # remove() does take a single parameter
    # Searches for the given element and removes it
    # If element isn't found is gives an error called KeyError
    # It doesnt return any value


'''

#work with remove()
lan = {"English", "French", "German"}
#remove() return vale is None
print(lan.remove("German"))
#printing the existing set item
print(lan)

#tring to delete which item isn't in set
#it gives an KeyError : 'shh'
animal = {"cat", "cow", "dog", "rabbit"}
print(animal.remove("shh"))


