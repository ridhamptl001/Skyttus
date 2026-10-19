
class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal name:", self.name)



class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        super().display()
        print("Breed:", self.breed)



dog = Dog("Tommy", "Labrador")
dog.display()
