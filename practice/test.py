from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


p1 = CreditCardPayment()
p1.pay(500)   # Paid 500 using Credit Card

p2 = UPIPayment()
p2.pay(200)   # Paid 200 using UPI



