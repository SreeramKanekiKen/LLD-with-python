from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
        
    @abstractmethod
    def pay(self):
        ...
        
class CreditCardPayment(Payment):
    def pay(self):
        print(f"Paying {self.amount} using Credit Card.")
        
class PayPalPayment(Payment):
    def pay(self):
        print(f"Paying {self.amount} using PayPal.")  
        
class DebitCardPayment(Payment):
    def pay(self):
        print(f"Paying {self.amount} using Debit Card.")
        
if __name__ == "__main__":
    payment1 = CreditCardPayment(100)
    payment1.pay()
    
    payment2 = PayPalPayment(200)
    payment2.pay()
    
    payment3 = DebitCardPayment(300)
    payment3.pay()