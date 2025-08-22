class ShapeCalculator:
    def calculate_area(shape):
        if (shape.type == "Rectangle"):
            return shape.width * shape.height
        elif (shape.type == "Circle"):
            return 3.14 * (shape.radius ** 2) 
    
    def calculate_perimeter(shape):
        if (shape.type == "Rectangle"):
            return 2 * (shape.width + shape.height)
        elif (shape.type == "Circle"):
            return 2 * 3.14 * shape.radius
        
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        ...
    
    @abstractmethod
    def calculate_perimeter(self):
        ...
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
if __name__ == "__main__":
    rectangle1 = Rectangle(10, 20)
    
    print(rectangle1.calculate_area())
    print(rectangle1.calculate_perimeter())
    
    print("--------------------------------------")
    
    cirlce1 = Circle(5)
    
    print(cirlce1.calculate_area())
    print(cirlce1.calculate_perimeter())