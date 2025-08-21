class Car:
    #constructor
    
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        
        
    #Method to display car Details
    def displayInfo(self):
        print(f"Car Color:" {self.color})
        print(f"Car Make:" {self.make})
        print(f"Car Model:" {self.model})
        print(f"Car Year:" {self.year})        