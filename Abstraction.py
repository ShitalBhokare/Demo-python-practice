# Abstraction means hiding the internal implementation details 
# and showing only the essential features to the user.
# For example, when a user starts the car, they see only "Car started" message,
# but they don't need to know the internal steps like engaging the clutch or accelerator.

class Car:
    def __init__(self):
        self.accl = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.accl = True
        print("Car started....")
        
car1 = Car()
car1.start()
