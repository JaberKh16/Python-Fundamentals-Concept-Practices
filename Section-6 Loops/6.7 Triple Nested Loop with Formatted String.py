"""
    Syntax -->  for var1 in iterable1:
                    for var2 in iterabl2:
                        for var3 in iterabl3:
                        
    For Example- 
                for i in range(2):
                    for j in range(5):
                        for k in range(3):
                            print("")
"""

# Declaring some Iterables
products = ['Product A', 'Product B'] # to represent products
prod_sales = [10000, 34000, 23000, 53000, 50000] # to represent sales
time_horizon = (1, 3, 12) # to represent monthly, quartly, yearly

for prod in products:
    for pr_sales in prod_sales:
        for t_zon in time_horizon:
            print("Expected sales for a period of {0} month(s) for {1}: ${sales}".format(t_zon, prod, sales = prod_sales*t_zon)) 

