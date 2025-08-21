class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
        
    def eat(self):   
        print(f"{self.name} is eating dog food.")  
        super().eat()
        
class GermanShepherd(Dog):
    def bark(self):
        print(f"{self.name} is barking loudly.")
        
    def eat(self):
        super().eat()  
        print(f"{self.name} is eating German Shepherd food.")
        
class Labrador(Dog):
    def bark(self):
        print(f"{self.name} is barking slowly.")
        
    def eat(self):
        super().eat()  
        print(f"{self.name} is eating meat")
        
class MyDog(GermanShepherd, Labrador):
    def eat(self):
        print(f"{self.name} is eating a mix of German Shepherd and Labrador food.")
        super().eat()
        
if __name__ == "__main__":
    my_dog = MyDog("rocky")
    my_dog.bark()   
    
    