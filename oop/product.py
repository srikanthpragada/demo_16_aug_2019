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

    @property
    def netprice(self):
        return self.price + self.price * Product.taxrate / 100

    def __str__(self):
        return f"{self.name} - {self.price}"


    def __eq__(self, other):
        return self.name == other.name  and self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 80000)
print(p1.netprice)  # Property


# p2 = Product("Laptop", 70000)
#
# print(p1 == "abc")
#
# print(p1 != p2)
# print(p1 > p2)
# print(str(p1))
