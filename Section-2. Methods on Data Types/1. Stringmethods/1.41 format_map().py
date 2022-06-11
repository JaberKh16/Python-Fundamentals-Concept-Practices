"""
    String Method: format_map()
    ===========================
    # Syntax : str.format_map( mapping )
    # format_map() does take a single parameter which is needed to be passed.
    # Parameter (mapping) have to be dict_type
    # The format_map() is similar to str.format(mapping) excepts
      that it is( str.format(mapping)) creates new dict type.
    # Note: format_map(mapping) doesn't create a new dict
            whereas it pass the reference address of the dict key's

    # It returns the Key's Values of dict_type
    # Useful when working with dict subclass

"""

p = { "x": 4, "y" : -5}
print(p)
print("{x}{y}".format_map(p))
print("{y}".format_map(p))