from abc import ABC, abstractmethod

#define an interface
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...
    
    @abstractmethod
    def stop(self):
        ...
        
class Vehicle_Registration(ABC):
    @abstractmethod
    def register(self):
        ...
        
    
#implement the vehicle interface
class Car(Vehicle_Registration, Vehicle):
    #Method to start the car
    def register(self):
        print("the car has been registered")
        
    def start(self):
        print("the car has started")
        
    #Method to stop the car
    def stop(self):
        print("the car has stopped")
        

class Payment(ABC):
    @abstractmethod
    def pay(self):
        ...
        
    def refund(self):
        print("Payment refunded")
        
class CashPayment(Payment):
    def pay(self):
        print("Payment made in cash")
        
class CardPayment(Payment):
    def pay(self):
        print("Payment made using card")
        

if __name__ == "__main__":
    myCar = Car()
    myCar.start()
    myCar.stop()
    myCar.register()   
    
    cash_payment = CashPayment()
    cash_payment.pay()     
    cash_payment.refund()    
    
    card_payment = CardPayment()
    card_payment.pay() 
    
    #This will raise an error as Vehicle is an abstract class and cannot be instantiated
    #vehicle = Vehicle()