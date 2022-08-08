"""
    Instance And Class Attributes Concept
    =====================================
    In Python, Attributes can be broadly categorized into two types
    which are the following-
        1) Class Attributes -- declared outside the class methods
        2) Instance Attributes -- declared inside the class methods
    
    Class attributes are shared by all the objects of a class while 
    instance attributes are the exclusive property of the instance.

    Remember, an instance is just another name for the object. 
    Instance attributes are declared inside any method while 
    class attributes are declared outside of any method. 
    
    Instance attributes are referred using the 'self' keyword, while 
    Class attributes are referred by the class name.

    Accessing of Clas Attributes can be done either using the class 
    name or with the class instances. If its inside the class methods
    then need to be accessed through the class name with a dot operator
    and if its needs to access through the class instance then it can
    also be done using the class instance name.
    
"""

# defining the class
class Car:
    
    # class attribute
    car_brand = 'Toyota' 
    car_count = 0
    def car_data(self):
        # class instances attributes
        self.car_name = 'GT-500' 
        # print(f'Car Name : {self.car_name}')
        self.fuel_capacity = 34.5
        # print(f'Car Fuel Capacity :{self.fuel_capacity}')
        Car.car_count +=1 # accesing the class attributes with class name
        
    def get_car_information(self):
        
        # 'self' is accessible whole over the class lifespan
        print(f'Car Name : {self.car_name}')
        print(f'Car Fuel Capacity :{self.fuel_capacity}')
        
# creating the instance
car = Car()

# accessing class methods through class instance
car.car_data()
car.get_car_information()

# accessing class attributes
print(Car.car_brand)
