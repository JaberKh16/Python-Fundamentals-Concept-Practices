'''
    itertools.cycle() Function
    ==========================
    # Itertools function cycle(), cycles through an an iterator endlessly.
      Syntax- 
            itertools.cycle(iterable)

    # To stops iteration we have to check it with last index value of string
      where we want to stop, we need to specify it through a conditon.

'''

# working with string data_type
from itertools import cycle
for i in cycle("Message"):
    print(i)
    if i =="g" : # reached the last character
        break

# working with list data_type
from itertools import cycle
# defining an iterable
random_list_items = [1, 2, 4, "a", "Orange", "Apple"] 
for i in cycle(random_list_items):
    # print(i) # uncomment it and see it goes through endlessly
    if i == "a":
      break

