"""
    Clas Instance Methods and Static Method Concept
    ===============================================
    There are 2 types of methods within a class. Those are following:
    
        a) Instance Methdos: 

            1.  Instance methods are defined inside a class and are used 
                to get the contents for an instance.
            2.  They can also be used to perform operations with the attributes 
                of the objects.
            3.  Whatever methods we described by 'self' is an instance methods or 
                can say non static methods are the instance methods.
            
    b) Static Methods:
        
        1.  Static methods are created using '@staticmethod' decorator.
        2.  Decorator is the functions that takes another function and extends
            its functionality.
        3.  A static method basically doesn't need the reference argument
            (pass arguments via obj) means can directly call without using 
            class instance object. These methods can be called via 
            class name directly or using class object also, both are 
            permissible.
"""

# defining the class
class Racer:
    
    # class attributes
    racer_participation_tournament = 'World Sports Car Championship'
    
    # using instance attributes here within the class constructor
    def __init__(self, racer_name, racer_car_name, racer_car_fuel_capacity, racer_experience) :
        self.racer_name = racer_name
        self.racer_car_name = racer_car_name
        self.racer_car_fuel_capacity = racer_car_fuel_capacity
        self.racer_experience = racer_experience
        
    # class instance methods
    def show_racer_details(self):
        print(f'Racer Name : {self.racer_name}')
        print(f'Racer Experience : {self.racer_experience}')
    
    def car_details(self):
        print(f'Car Name : {self.racer_car_name}')
        print(f'Car Fuel Capacity in Litre : {self.racer_car_fuel_capacity}')
    
    # class static methods
    @staticmethod
    def particapators_information():
        print('Welcome to the Sports Car Championship')
        

# getting all inputs for the show_racer_function()
racer_name = input('Enter the Racer Name :')
racer_car_name = input('Enter the Racer Car Name:')
racer_car_fuel_capacity = float(input('Enter the Car Fuel Capacity In Litres:'))
racer_experience = int(input('Enter the Racer Racing Experience: '))

# creating a class object
player_1 = Racer( racer_name, racer_car_name, 
                racer_car_fuel_capacity, racer_experience)

print('============================================================')

# getting racer details
print('Racer Infomation  :{} '.format(player_1))
player_1.show_racer_details()
# getting car details
print('Car Infomation   :{} '.format(player_1))
player_1.car_details()


# calling way of static methods
# first calling via the reference object
player_1.particapators_information()
# secondly calling via the class name
Racer.particapators_information()