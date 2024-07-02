from factory import *

def main():
    # Crear vehículos usando la fábrica
    car = VehicleFactory.create_vehicle("car")
    bike = VehicleFactory.create_vehicle("bike")
    motorcycle = VehicleFactory.create_vehicle("motorcycle")

    # Usar los vehículos
    print(car.move())         
    print(bike.move())       
    print(motorcycle.move())  

    try:
        unknown = VehicleFactory.create_vehicle("plane")
    except ValueError as e:
        print(e)  

if __name__ == "__main__":
    main()