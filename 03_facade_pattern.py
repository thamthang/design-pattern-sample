class Discount:
    def calculate(self, value):
        return value * 0.9

class Fees:
    def calculate(self, value):
        return value * 1.05

class ShippingCost:
    def calculate(self):
        return 5
    
class Purchase:
    def __init__(self):
        self.discount = Discount()
        self.fees = Fees()
        self.shipping_cost = ShippingCost()

    def calculate(self, price):
        price = self.discount.calculate(price)
        print(f'Price after discount: {price}')
        price = self.fees.calculate(price)
        print(f'Price after fees: {price}')
        price += self.shipping_cost.calculate()
        print(f'Final price: {price}')

if __name__ == '__main__':
    purchase = Purchase()
    purchase.calculate(100)
