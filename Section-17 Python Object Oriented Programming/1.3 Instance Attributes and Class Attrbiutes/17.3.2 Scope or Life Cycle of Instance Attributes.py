"""
    Scopes Of Instance And Local Attributes Concept
    ================================================
    Instance Attributes has its scope throghout the class wherever
    its being defined. Instance Attributes are those which generally
    are being defined inside a class methods and having the keyword
    'self' thus its has its scope throughout the class.
    
    Where the Local Attributes are those attributes which is defined
    only inside the class methods and has no 'self' keyword with them
    while defining. These are the temporary variables for the class
    methods and has its scope only inside the methods where its being 
    defined, thus can't be accessible outside that class method.
    
"""

# Scope of the instance variables
class Car:
    def car_data(self):
        self.car_name = 'GT-500'
        print(f'Car Name : {self.car_name}')
        fuel_capacity = 34.5 # class local variable
        print(f'Car Fuel Capacity :{fuel_capacity}')
    
    def get_car_information(self):
        
        # 'self' is accessible whole over the class lifespan
        print(f'Car Name : {self.car_name}')
        try:
            # see local variables is only accessible to that function
            # where its being specified
            print(f'Car Fuel Capacity :{fuel_capacity}')
        except Exception as e:
            print(e)
        

# creating the class instance
car = Car()

# accessing class instance methods
car.car_data()
car.get_car_information()

