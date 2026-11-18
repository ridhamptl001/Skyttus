
class Father:
    def skills1(self):
        print("Father knows driving")

class Mother:
    def skills2(self):
        print("Mother knows cooking")

class Child(Father, Mother):
    def own_skill(self):
        print("Child knows painting")
child = Child()

child.skills1()
child.skills2()
child.own_skill()
