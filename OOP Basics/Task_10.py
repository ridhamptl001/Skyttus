
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        product = {
            "name": name,
            "price": price
        }

        self.products.append(product)
        print("Product added successfully.")

    def list_products(self):
        print("Shop Products:")

        for product in self.products:
            print(product["name"], "- ₹", product["price"])


shop1 = Shop()

shop1.add_product("Keyboard", 800)
shop1.add_product("Mouse", 400)
shop1.add_product("Monitor", 7000)


shop1.list_products()
