from builder import *

if __name__ == "__main__":
    director = Director()

    gaming_builder = ComputerBuilder("GAMING-001")
    gaming_computer = director.construct_gaming_computer(gaming_builder)

    office_builder = ComputerBuilder("OFFICE-001")
    office_computer = director.construct_office_computer(office_builder)

    print("Gaming Computer:")
    print(gaming_computer)

    print("\nOffice Computer:")
    print(office_computer)


