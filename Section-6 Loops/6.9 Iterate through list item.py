"""
    Creating List Throgh The range() Function
"""

# first creating a range object which store range(1, 11)
# then convert this to list object
list_1 = list(range(1, 11)) # list will store [1, 2, ...,10]
print(f"List Items are : {list_1}")
print(f"Length is:{len(list_1)}")

# iterate through the list
for items in range(len(list_1)):
    print(items + 1, end=" ")
