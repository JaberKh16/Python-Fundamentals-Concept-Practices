'''
    # Syntax : list.sort( key =..., reverse=...)
    # sort() does take two parameters
    # Sort can be done with same type of data_type
    # It sorts the element of given list
    # It usually sorts the element in descending order
    # By default sort() doesn't require any parameter
    # sort() doesn't return any value, where sorted() does,
      sorted returns a iterable list
    # sort() can update the original list
    # And to back the original list we have to use sorted()
    # When no parameter is being passed is returns the unsorted same
      given list
    #Setting parameter,  list.sort(reverse = True) sort the list
     in descending order
    # it doesn't return any value, it returns None


'''

#works with sort()
#When no parameter is being passed
# returns the same list unsorted
vowels = ["a", "e", "i", "o", "u"]
print(vowels)
print("Return Value :", vowels.sort())
print("Sorted List :", vowels)

#When one parameter is being passed
#parameter , set it (reverse=True)
#returns the sorted list

vowels = ["a", "e", "i", "o", "u"]
print(vowels)
print("Return Value :", vowels.sort(reverse=True))
print("Sorted List(in descending) order :", vowels)

#When u want to manually sort the list
#key parameter is used for this action
#list.sort(key=len)
#the list is sorted based on the length of it's each element,
## ---> form lowest to highest

def take_Second(elem) :
    return elem[1]
random = [(2,2), (3, 4), (4,1), (1, 3), (15, 5)]
#sorted with key
print(random.sort(key=take_Second))
print("Sorted List :", random)