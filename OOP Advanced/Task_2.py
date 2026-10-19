
class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging.")


my_car = ElectricCar()

my_car.start()
my_car.drive()
my_car.charge()
