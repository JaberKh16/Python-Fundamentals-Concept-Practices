"""
 # Multilevel Inheritance: 
   
   Multilevel inheritance refers to a mechanism in OO technology, 
   where one can inherit from a derived class(previous class), thereby making  
   this derived class the base class for the new class. 
   For example- say, C is subclass or child class of B and B is a child class of A.


"""
class Galaxy:
    def __init__(self, galaxy_name,followed_star_name, followed_planet_name) -> None:
        self.galaxy_name = galaxy_name
        self.followed_star_name = followed_star_name
        self.followed_planet_name = followed_planet_name

class Earth(Galaxy):
    def __init__(self, planet_name,earth_size, earth_temparature) -> None:
        self.planet_name = planet_name
        self.earth_size = earth_size
        self.earth_temparature = earth_temparature
        super().__init__(galaxy_name = 'MilkyWay',followed_star_name='Sun', followed_planet_name='Earth')
    def planet_info(self):
        print(f'Earth Size : {self.earth_size}')
        print(f'Earth Temparature : {self.earth_temparature}')

class Moon(Earth):
    def __init__(self) -> None:
        super().__init__(planet_name='Earth',earth_size='6371 km',earth_temparature='0.9 degree')
        
    def get_all_info(self):
        print(f'Galaxy Name: {self.galaxy_name}')
        print(f'Followed Star Name: {self.followed_star_name}')
        print(f'Planet Name: {self.followed_planet_name}')
        super().planet_info()
        


moon = Moon()
moon.get_all_info()    