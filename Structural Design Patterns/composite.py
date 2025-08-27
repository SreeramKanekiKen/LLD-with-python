from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def get_price(self):
        ...
        
    @abstractmethod
    def get_description(self):
        ...
    
    
class Product(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_price(self):
        return self.price
    
    def get_description(self):
        return f"Product {self.name} ${self.price}"
    
# Composite Class:Box

class Box(Item):
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_item(self, item: Item):
        self.items.append(item)
        
    def remove(self, item: Item):
        self.items.remove(item)
        
    def get_price(self):
        total_price = 0
        
        for item in self.items:
            total_price += item.get_price()
            
        return total_price
    
    def get_description(self):
        description = [item.get_description() for item in self.items]
        return f"Box: {self.name} containing: \n " + "\n ".join(description)     
    
    
# Client Code

if __name__ == "__main__":
    #Leaf Products
    
    pen = Product("Pen", 2.5)
    notebook = Product("NoteBook", 5.0)
    charger = Product("Charger", 15.0)
    
    smallBox = Box("StationaryBox")
    smallBox.add_item(pen)
    smallBox.add_item(notebook)
    
    electronics_box = Box("ElectronicsBox")
    electronics_box.add_item(charger)
    
    # Big Box 
    
    mainbox = Box("Main Box")
    mainbox.add_item(smallBox)
    mainbox.add_item(electronics_box)
    mainbox.add_item(Product("USB Driver", 10.0))   
    
    print(mainbox.get_description())
    print(f"Total Price: {mainbox.get_price()}")
       