class Product:
    # Class attribute (static attribute)
    taxrate = 15

    # Static method
    @staticmethod
    def get_net_price(price):
        return price + price * Product.taxrate / 100

    # Constructor
    def __init__(self, name, price=0):
        # Object attributes
        self.name = name
        self.price = price

    # Methods
    def print_details(self):
        print(self.name, self.price)

    def net_price(self):
        return self.price + self.price * Product.taxrate / 100


p = Product("Laptop", 70000)
p.print_details()
print(p.net_price())

print(Product.get_net_price(15000))


