from abc import ABC, abstractmethod
"""
Thrid principle Loskov'a and that means if you have objects at program you should be able
to replace this objects with instances of their subtypes, or subclasses
without alterting the correctnes of the program
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
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_adreess):
        self.email_adreess = email_adreess

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
