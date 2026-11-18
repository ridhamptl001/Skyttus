
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

    def circumference(self):
        return 2*math.pi*self.radius
circle1 = Circle(7)

print("Area:", round(circle1.area(), 2))
print("Circumference:", round(circle1.circumference(), 2))
