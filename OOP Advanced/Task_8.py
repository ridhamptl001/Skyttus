
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching.")


class Student(Person):
    def study(self):
        print(self.name, "is studying.")


teacher = Teacher("Mr. Henil")
student = Student("Ridham")

teacher.display_name()
teacher.teach()

student.display_name()
student.study()
