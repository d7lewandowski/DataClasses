"""
SINGLE RESPONSIBILITY
"""


class Order:
    """
    We want classes and methond with single responsibiity, 
    class is reasponsible for only one thing and that ensured you can reuse them much easier later on
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
    
        
class PaymentProcessor:
    """
    PaymentProcessor class has one responsibility
    """

    def pay_credit(self, order, security_code):

        print("Processing debit payment type")
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'
 

        
    def pay_debit(self, order, security_code):
        
        print("Processing debit payment type")
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

order = Order()
order.add_item("Keyboard", 1, 58)
order.add_item("SSD", 1, 150)
order.add_item("USD cable", 2, 5)

print(order.total_price())

processor = PaymentProcessor()
processor.pay_credit(order, "34324324")
