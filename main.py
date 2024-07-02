from absfactory import *

def main(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()

    print(chair.sit_on())
    print(table.eat_on())

if __name__ == "__main__":
    print("Client: Testing client code with the ModernFurnitureFactory:")
    main(ModernFurnitureFactory())

    print("\nClient: Testing client code with the VictorianFurnitureFactory:")
    main(VictorianFurnitureFactory())