class Animal:
    def eat(self):
        print("animal is eating")
        
class dog(Animal):
    def bark(self):
        print("Dog is barking.")

class cat(Animal):
    def meow(self):
        print("Cat is meowing.")
    
dog=dog()
cat=cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()