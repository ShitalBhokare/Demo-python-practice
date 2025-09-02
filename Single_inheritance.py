# This example demonstrates single inheritance in Python.
# The Car class is the parent class with static methods to start and stop a car.
# The ToyotaCar class is the child class which inherits from Car.
# ToyotaCar has its own attribute 'name' but can access Car's methods like start() and stop().
# This shows how a child class can reuse and extend the functionality of a parent class.

class Car:
        
    @staticmethod
    def start():
        print("Car Started...")
        
    @staticmethod
    def stop():
        print("Car stopped...")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name=name
        
car1=ToyotaCar("Prius")
car2=ToyotaCar("Fortuner")
        
print(car1.name)
car1.start()
car1.stop()
    