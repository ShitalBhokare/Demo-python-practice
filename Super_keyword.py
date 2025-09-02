# The super() function is used to call the constructor of the parent class (Car) from the child class (ToyotaCar).
# It allows ToyotaCar to inherit and initialize attributes defined in Car.
# This avoids repeating code and ensures proper initialization of the inherited 'type' attribute.

class Car:
    def __init__(self, type):
        self.type=type
    
    @staticmethod
    def start():
        print("Car started...")
        
    def stop(self):
        print("Car Stopped...")
    
class ToyotaCar(Car):
    def __init__(self, type, brand):
        self.brand=brand
        super().__init__(type)
        
car1=ToyotaCar("Diesel","Toyota Innova")
car1.start()
print(car1.type)
print(car1.brand)
        
            
    