class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def available(self, quantity_requested):
        return self.quantity >= quantity_requested

    def reduce_stock(self, quantity_sold):
        self.quantity -= quantity_sold

class Cart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_product(self, product, quantity):
        if product.available(quantity):  # Updated here
            product.reduce_stock(quantity)
            self.items.append((product.name, quantity, product.price))
            self.total += product.price * quantity
            print(f"Added {quantity} x {product.name} to your cart.")
        else:
            print(f"Sorry, not enough stock for {product.name}.")

    def generate_receipt(self):
        print("\n--------- RECEIPT ---------")
        for item in self.items:
            name, quantity, price = item
            print(f"{name} x{quantity} - NRS {price * quantity:.2f}")
        print(f"\nTotal: NRS {self.total:.2f}")
        print("Thank you for shopping with us!\n")

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def shop(self, product_list):
        print(f"\n{self.name}'s Shopping Cart:\n")
        for product, quantity in product_list:
            self.cart.add_product(product, quantity)

    def checkout(self):
        self.cart.generate_receipt()

noodles = Product("Noodles", 20.0, 100)
biscuits = Product("Biscuits", 10.0, 50)
chocolates = Product("Chocolates", 15.0, 30)

# Example:

ram = Customer("Ram")
ram.shop([(noodles, 3), (biscuits, 5), (chocolates, 2)])
ram.checkout()

sita = Customer("Sita")
sita.shop([(noodles, 10), (chocolates, 40)])
sita.checkout()

hari = Customer("Hari")
hari.shop([(noodles, 5), (biscuits, 3), (chocolates, 10)])
hari.checkout()
