#Product (House)

class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None
        self.garden = None
        self.swimmingpool = None
        self.garage = None
        
    def __str__(self):
        return (f"House with {self.walls} walls, {self.doors} doors, {self.windows} windows, {self.roof} roof, {self.garden} garden, {self.swimmingpool} and {self.garage}")
   
   
    
#Builder Interface
from abc import ABC, abstractmethod

class HouseBuilder(ABC):
    @abstractmethod
    def reset(self):
        ...
        
    @abstractmethod
    def build_walls(self):
        ...
        
    @abstractmethod
    def build_doors(self):
        ...
        
    @abstractmethod
    def build_windows(self):
        ...
        
    @abstractmethod
    def build_roof(self):
        ...
        
    @abstractmethod
    def build_roof(self):
        ...
        
    @abstractmethod
    def add_garden(self):
        ...
        
    @abstractmethod
    def add_swimmingpool(self):
        ...
        
    @abstractmethod
    def add_garage(self):
        ...
        
    @abstractmethod
    def get_result(self):
        ...
        
#Concrete House Builder(Simple and Luxury Houses)

class SimpleHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.house = House()
    
    def build_walls(self):
        self.walls = 4
    
    def build_doors(self):
        self.doors = 1
        
    def build_windows(self):
        self.windows = 2
        
    def build_roof(self):
        self.roof = "Simple Roof"
        
    def add_garden(self):
        self.garden = False
        
    def add_swimmingpool(self):
        self.swimmingpool = False
        
    def add_garage(self):
        self.garage = False
        
    def get_result(self):
        return self.house
    
    
#Luxury House


class LuxuryHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.house = House()
    
    def build_walls(self):
        self.walls = 8
    
    def build_doors(self):
        self.doors = 4
        
    def build_windows(self):
        self.windows = 10
        
    def build_roof(self):
        self.roof = "Luxury Roof"
        
    def add_garden(self):
        self.garden = True
        
    def add_swimmingpool(self):
        self.swimmingpool = True
        
    def add_garage(self):
        self.garage = True
        
    def get_result(self):
        return self.house
    
#Director 
class Director:
    def __init__(self, builder:HouseBuilder):
        self.builder = builder
        
    def construct_simple_house(self):
        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
    
    def construct_luxury_house(self):
        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
        self.builder.add_garden()
        self.builder.add_swimmingpool()
        self.builder.add_garage()
        
#Client Code
if __name__ == "__main__":
    simple_house_builder = SimpleHouseBuilder()
    director = Director(simple_house_builder)
    director.construct_simple_house()
    simple_house = simple_house_builder.get_result()
    print(f"Simple House: {simple_house}")
    
    luxury_house_builder = LuxuryHouseBuilder()
    director = Director(luxury_house_builder)
    director.construct_luxury_house()
    luxury_house = luxury_house_builder.get_result()
    print(f"Luxury House: {luxury_house}")
    
    
    
    
        
    