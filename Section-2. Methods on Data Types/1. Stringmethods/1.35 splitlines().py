"""
    String Method: splitlines()
    ===========================
    # Syntax : str.splitlines( [keepends] )
    # splitlines() does take a single parameter.
    # Keepends (argument) has single boolean type value which is 'True'.
    # Keepends (argument) also gives the item of unicode escape sequence
      in a List.
    # Returns a List Data_Type of given String Data_Type.
    # It splits the string at line breaks means (escape sequence)
      if it's been given as (separator) string and returns a List of lines
    # This method splits the string starting form the right at the
    specified  (separator)
    # When no line breaks (escape sequence) is given in the string
      it returns the string of list with single item.

    # When no argument is passed it gives the list
      one item of given string (single str) List e.g  [ 'given str' ]

"""

# with no parameter specified
grocery = "Milk\r\nChicken\t\nBread\a\v\u2029Butter\x85\x1e"
print(grocery)
r = grocery.splitlines()
print("Escape Sequence is given:", r)

# when (keepends) parameter is being specified
r = grocery.splitlines(True)
print("Keepend is given as Parameters", r)

# When given string has no line break it returns the  single item 
# of given string as List --> e.g  [ 'given str' ] with no parameter specified
t = "Milk, Bread, Bread, Butter"
print(t)
r = t.splitlines()
print(r)

# Keepend is being passed so it will returns the same given string
r =t.splitlines(True)
print(r)
