"""
    This is an another example of Nested Loop.
"""
# defining the variable
products = ['Product A', 'Product B']
prod_sales = [10000, 20000, 30000, 40000, 50000]

for prod in products:
    for pr_sales in prod_sales:
        print([prod,pr_sales])
