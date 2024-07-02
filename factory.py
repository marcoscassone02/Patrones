class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving a car"

class Bike(Vehicle):
    def move(self):
        return "Riding a bike"

class Motorcycle(Vehicle):
    def move(self):
        return "Riding a motorcycle"
    
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")