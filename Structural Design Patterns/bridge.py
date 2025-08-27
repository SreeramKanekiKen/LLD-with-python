from abc import ABC, abstractmethod

# Implementation Interface

class Color(ABC):
    @abstractmethod
    def apply_color(self):
        ...
        
# Concrete Implementation

class Red(Color):
    def apply_color(self):
        return "RED"
    
class Blue(Color):
    def apply_color(self):  
        return "BLUE"
        
        
# The Abstraction Hierarchy -> shape

class Shape(ABC):
    def __init__(self, color:Color):
        self.color = color
        
    @abstractmethod
    def draw(self):
        ...
        
class Circle(Shape):
    def draw(self):
        print(f"Drawing a {self.color.apply_color()} Circle")
        
class Rectangle(Shape):
    def draw(self):
        print(f"Drawing a {self.color.apply_color()} Rectangle")
        

# Client Code

if __name__ == "__main__":
    red = Red()
    blue = Blue()
    
    red_circle = Circle(red)
    blue_rectangle = Rectangle(blue)
    
    red_circle.draw()
    blue_rectangle.draw()