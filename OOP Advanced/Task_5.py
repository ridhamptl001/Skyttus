
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

class Rectangle:
    def area(self):
        return 6 * 3


def show_area(shape):
    print("Area:", shape.area())



circle = Circle()
square = Square()
rectangle = Rectangle()

show_area(circle)
show_area(square)
show_area(rectangle)
