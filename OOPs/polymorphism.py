class MathOperation:
    def add(self, a, b, c=0, *args):
        sumx = a + b + c
        for each in args:
            sumx += each
        
        return sumx
    
math = MathOperation()
print("Sum of 2 numbers: ", math.add(5, 10))
print("Sum of 3 numbers: ", math.add(5, 10, 15))
print("Sum of 5 numbers: ", math.add(5, 10, 15, 20, 25))

class Animal:
    def make_sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")
        
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")
        
animals = [Dog(), Cat()]

