# This code shows multilevel inheritance in Python.
# Car is the base class with a static start method and an instance stop method.
# ToyotaCar inherits from Car and adds a brand attribute.
# Fortuner inherits from ToyotaCar and adds a type attribute.
# The Fortuner constructor uses super() to initialize the brand.
# An instance of Fortuner is created with brand and type values.
# Methods and attributes are accessed from the instance.


class Car:
    @staticmethod
    def start():
        print("Car Started")
        
    def stop(self):
        print("Car Stopped")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand =brand
        
class Fortuner(ToyotaCar):
    def __init__(self,brand, type):
        super().__init__(brand)
        self.type=type

car1=Fortuner("Toyota Innova","diesel")
print(car1.type)
car1.start()

print(car1.brand)