from abc import ABC, abstractmethod
"""
Interface segregation means overall is better if you have serval specifcy interfaces
as supposted to have one genearal interface
"""
class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'


    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True 

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code

    def auth_sms(self, code):
        raise Exception("Credit card payments don't support SMS code auth")

    def pay(self, order):
        print("Processing credit payment type")
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_adreess):
        self.email_adreess = email_adreess

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True 

    def pay(self, order):
        print("Processing paypal payment type")
        print(f'Verifying security code: {self.email_adreess}')
        order.status = 'paid'


        
order = Order()
order.add_item("Keyboard", 1, 58)
order.add_item("SSD", 1, 150)
order.add_item("USD cable", 2, 5)

print(order.total_price())
payment = PaypalPaymentProcessor("dam@lew.com")
payment.pay(order)
