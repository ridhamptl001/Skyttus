
class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        average = (self.marks1+self.marks2+self.marks3) / 3
        return average

    def display(self):
        print("Student:", self.name)
        print("Average marks:", self.average())
student1 = Student("Ridham", 80, 90, 85)
student1.display()
