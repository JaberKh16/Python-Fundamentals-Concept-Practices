"""
  Multiple Inheritance:
    # A class which is get inherited from a multiple classes means where 
      a class inherits from more than one base class.
    # Multilevel Inheritance is an Inheritance type that 
    # inherits from a derived class, making that derived class
    # a base class for a new class.

"""


class Mobile:
    
    def __init__(self, mobile_os, mobile_brand, mobile_type) -> None: 
        self.mobile_os = mobile_os
        self.mobile_brand = mobile_brand
        self.mobile_type = mobile_type
    
    def mobile_info(self):
        print(f'Mobile OS:{self.mobile_os}')
        print(f'Mobile model:{self.mobile_brand}')
        print(f'Mobile Type:{self.mobile_type}')
        

class Android(Mobile):
    def __init__(self, model_name, model_price) -> None:
        # model_name = input('Enter the Model Name :')
        # model_price = int(input('Enter the Model Price:'))
        self.model_name = model_name
        self.model_price = model_price
        # accessing parent class using super().parent_class_method_name()
        # set the initializer value from child class
        super().__init__(mobile_os='Android', mobile_brand='Samsung', mobile_type='Flat')
        super().mobile_info()
    def model_info(self):
        
        print(f'Model Name :{self.model_name}')
        print(f'Model Price :{self.model_price}')
        
class Model_Features(Android, Mobile):
    def __init__(self, ram_info, rom_info, processor_clock_rate,display_type) -> None:
        self.ram_info = ram_info
        self.rom_info = rom_info
        self.processor_clock_rate = processor_clock_rate
        self.display_type = display_type
        super().__init__(model_name='Duos 2x', model_price=18000)
        super().model_info()
    
    def get_features_info(self):
        print(f'Model Ram Info :{self.ram_info}')
        print(f'Model Rom Info :{self.rom_info}')
        print(f'Model Processor Clock Info :{self.processor_clock_rate}')
        print(f'Model Display Type :{self.display_type}')
        self.other_features()
        
    def other_features(self):
        battery = '5000 Lithium Polymer'
        supported_network = '4G'
        camera = 'Enabled'
        print(f'Model Battery Info:{battery}')
        print(f'Model Supported Info:{supported_network}')
        print(f'Model Camera Info:{camera}')
 
samsung = Model_Features('4GB', '2GB', '2.3GHz', 'LCD')
samsung.get_features_info()

             