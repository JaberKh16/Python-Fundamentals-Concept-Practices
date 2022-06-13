"""
    Global Variables Inside A Nested Function
"""

# defining the function
def city_name_printing():
    city_name = "Itally"
    def update_city_name():
        global city_name
        city_name = "Franch"
    print("Before calling update_city_name(): " + city_name)
    print("Calling update_city_name() now:")
    
    # calling the nested function update_city_name()
    update_city_name()
    print("After calling update_city_name(): " + city_name)

# calling the function    
city_name_printing()
print("Value of 'city' inside the city_name_printing(): " + city_name)