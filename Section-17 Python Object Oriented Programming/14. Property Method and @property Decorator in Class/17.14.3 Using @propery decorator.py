
class House:

	def __init__(self, price=60000):
		self._price = price

    # this is basically the getter method for @property
	@property
	def price(self):
		return self._price
	
    # this is the setter method for @property
	@price.setter
	def price(self, new_price):
        # set new price only if the new_price is > 0 and type is float
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")
    # this is the deletter method for @property
	@price.deleter
	def price(self):
		del self._price
  
house = House()

# accessing instance attributes
print(f'House Price is: {house._price}')


# setting the price value using the setter method
# here, the @price.setter method is being called
house.price = 70000.00
# getting the value again
print(f'Updated Hosue Price is : {house.price}')


