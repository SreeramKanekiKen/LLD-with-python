#Abstract Method Interface
from abc import ABC, abstractmethod

#Chair Interface
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        ...
        
#Sofa Interface
class Sofa(ABC):
    @abstractmethod
    def ly_on(self):
        ...
        
#CoffeeTable Interface
class CoffeeTable(ABC):
    @abstractmethod
    def place_things(self):
        ...
        

#Concrete Product  Variant
#Modern Furniture

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on Modern Chair"
    
class ModernSofa(Sofa):
    def ly_on(self):
        return "Lying on Modern Sofa"
    
class ModernCoffeeTable(CoffeeTable):
    def place_things(self):
        return "Placed on Modern Coffee Table"
    
#Victorian Furniture

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on Victorian Chair"
    
class VictorianSofa(Sofa):
    def ly_on(self):
        return "Lying on Victorian Sofa"
    
class VictorianCoffeeTable(CoffeeTable):
    def place_things(self):
        return "Placed on Victorian Coffee Table"

#Art Deco Furniture

class ArtDecoChair(Chair):
    def sit_on(self):
        return "Sitting on Art Deco Chair"
    
class ArtDecoSofa(Sofa):
    def ly_on(self):
        return "Lying on Art Deco Sofa"
    
class ArtDecoCoffeeTable(CoffeeTable):
    def place_things(self):
        return "Placed on Art Deco Coffee Table"
    
    
#Abstract Factory Interface

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        ...
        
    @abstractmethod
    def create_sofa(self) -> Sofa:
        ...
        
    @abstractmethod
    def create_coffeetable(self) -> CoffeeTable:
        ...
        
#Concrete Factories
#Modern Furniture Family

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    
    def create_sofa(self):
        return ModernSofa()
    
    def create_coffeetable(self):
        return ModernCoffeeTable()
    
#Victorian Furniture Family
class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    
    def create_sofa(self):
        return VictorianSofa()
    
    def create_coffeetable(self):
        return VictorianCoffeeTable()
    
#Art Deco Furniture Family
class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ArtDecoChair()
    
    def create_sofa(self):
        return ArtDecoSofa()
    
    def create_coffeetable(self):
        return ArtDecoCoffeeTable()
    
#Client Code

class FurnitureStore:
    def __init__(self, factory:FurnitureFactory):
        self.chair = factory.create_chair()
        self.sofa = factory.create_sofa()
        self.coffeetable = factory.create_coffeetable()
        
    def show_furniture(self):
        print(self.chair.sit_on())
        print(self.sofa.ly_on())
        print(self.coffeetable.place_things())
        
if __name__ == "__main__":
    style = input("Enter Furniture Style (modern/victorian/art deco)").strip().lower()
    
    if style == "modern":
        factory = ModernFurnitureFactory()
        
    elif style == "victorian":
        factory = VictorianFurnitureFactory()
        
    elif style == "artdeco":
        factory = ArtDecoFurnitureFactory()
        
    else:
        print("Invalid Style")
        
    store = FurnitureStore(factory)
    store.show_furniture()
    
    