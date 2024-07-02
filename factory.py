class Vehicle:   #Product
    def move(self):
        pass

class Car(Vehicle):   #ConcreteProduct
    def move(self):
        return "Driving a car"

class Bike(Vehicle):   #ConcreteProduct
    def move(self):
        return "Riding a bike"

class Motorcycle(Vehicle):   #ConcreteProduct
    def move(self):
        return "Riding a motorcycle"
    
class VehicleFactory:   #Creator
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":   #ConcreteCreator
            return Car()
        elif vehicle_type == "bike":    #ConcreteCreator
            return Bike()
        elif vehicle_type == "motorcycle":    #ConcreteCreator
            return Motorcycle()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")