class car:
    def __init__(self, brand, model, speed):
        self.brand=brand
        self.model=model
        self.speed=speed
    
    def accelerate(self):
        self.speed+=10
        print("the car is moving",self.speed)
        
    def brake(self):
            self.speed-=10
            
            if self.speed<0:
                self.speed=0
                
                print("the car has stopped")
                
    def display(self):
                    print("brand:",self.brand)
                    print("model:",self.model)
                    print("speed:",self.speed)
                    
my_car=car("KIA","seltos",50)
my_car.display()
my_car.accelerate()
my_car.brake()