from abc import ABC, abstractmethod


class Order:
    """
    Second principle: Open / closed 
    that means we want to write code is open for extenstion but closed for modification
    """
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
    
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f'Verifying security code: {security_code}')
            self.status = 'paid'
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f'Verifying security code: {security_code}')
            self.status = 'paid'
        else:
            raise Exception(f'Unknown payment type: {payment_type}')

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):

    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'



order = Order()
order.add_item("Keyboard", 1, 58)
order.add_item("SSD", 1, 150)
order.add_item("USD cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor()
processor.pay(order, "035743")

