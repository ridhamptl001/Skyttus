class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        
employee1=employee("Ridham",21,30000)

employee1.display()
