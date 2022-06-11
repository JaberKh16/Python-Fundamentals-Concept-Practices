"""
    Example Of Iterate Through A Dictionary
"""

# prices dictinary contains the prices about the food
prices = {
    "hamburger": 200,
    "pizza" :  355,
    "sandwich" : 50 
}

# quantity contains the quantity information about the food have been bought
quantity = {
    "hamburger": 3,
    "pizza" : 1,
    "sandwich" : 4
}

# wanted to canlcuate how much spent over the food
# need to calculate prices[i] * quantity[i]
money_spent = 0  # initially spent money is 0
for i in prices:
    money_spent = money_spent + (prices[i] * quantity[i])

print(f"Total Money Spent over the food is: {money_spent}")