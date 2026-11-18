
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: ₹", self.price)


book1 = Book("Python", "Ridham Patel", 450)

book1.details()
