class Vehicle:
    def start(self):
        raise NotImplementedError
        
class Car(Vehicle):
    def start(self):
        print("Started the engine")
        
class Cycle(Vehicle):
    def repair(self):
        print("Repaired the cycle")
        
if __name__ == "__main__":
    car1 = Car()
    car1.start()
    
    cycle1 = Cycle()
    cycle1.start()