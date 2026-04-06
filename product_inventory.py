class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, qty):
        self.quantity += qty

    def show(self):
        print(self.name, "- Price:", self.price, "Qty:", self.quantity)


p1 = Product("Laptop", 50000, 10)
p1.update_quantity(5)
p1.show()