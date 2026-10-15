
class Laptop:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price

    def discount(self, discount):
        discount_amount = self.price*discount / 100
        final_price = self.price-discount_amount
        return final_price


laptop1 = Laptop("Dell", 50000)
final_price = laptop1.discount(10)

print("Brand:", laptop1.brand)
print("Original price:₹", laptop1.price)
print("Price after discount:₹", final_price)
