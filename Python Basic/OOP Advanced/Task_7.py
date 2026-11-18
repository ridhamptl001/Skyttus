
class Student:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age.")


student = Student(16)

print("Age:", student.get_age())

student.set_age(21)

print("Updated age:", student.get_age())
