"""
    This a another example of Triple Nested Loop.
    Syntax -->  for var1 in iterable1:
                    for var2 in iterabl2:
                        for var3 in iterabl3:
                        
    For Example- 
                for i in range(2):
                    for j in range(5):
                        for k in range(3):
                            print("")
"""

products = ['Product A', 'Product B']
prod_sales = [10000, 34000, 23000, 53000, 50000]
time_horizon = (1, 2, 3)

for prod in products:
    for pr_sales in prod_sales:
        for t_zon in time_horizon:
            print([prod, pr_sales, t_zon])
