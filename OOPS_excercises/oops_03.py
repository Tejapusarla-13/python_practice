#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

     def __init__(self, name, max_speed, mileage):
         self.name = name
         self.max_speed = max_speed
         self.mileage = mileage
        
class Bus(Vehicle):
     def get_vehicle_details(self):
         print("vehicle name: ",self.name)
         print("speed : ",self.max_speed)
         print("mileage : ",self.mileage)
