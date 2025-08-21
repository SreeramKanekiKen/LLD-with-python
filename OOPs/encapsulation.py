class BankAccount:
    def __init__(self):
        self.__account_holder = ""
        self.__balance = 0
        
    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")
            
    def get_account_holder(self):
        return self.__account_holder
            
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")
            
            
class PaymentProccess:
    def __init__(self, card_number, amount):
        self.__card_number = self.__mask_card_number(card_number)
        self.__amount = amount
            
    def __mask_card_number(self, card_number):
        return "**** **** **** " + card_number[-4:]
    
    def process_payment(self):
        if self.__amount > 0:
            print(f"Processing payment of {self.__amount} using card {self.__card_number}")
        else:
            print("Invalid payment amount")
            
if __name__ == "__main__":
    account1 = BankAccount()
    account1.set_account_holder("Sreeram")
    account1.set_balance(1000)
    print("Account Holder:", account1.get_account_holder())
    account1.deposit(500)
    print("New Balance:", account1.get_balance())
    
    print("------------------------------------")
    
    payment = PaymentProccess("1234 5678 9444", 500)
    payment.process_payment()
    