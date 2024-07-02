from abc import ABC, abstractmethod

class Chair(ABC):       # Abstract product
    @abstractmethod
    def sit_on(self):
        pass

class Table(ABC):       # Abstract product
    @abstractmethod
    def eat_on(self):
        pass

class ModernChair(Chair):       # Concrete product
    def sit_on(self):
        return "Sitting on a modern chair"

class VictorianChair(Chair):        # Concrete product
    def sit_on(self):
        return "Sitting on a Victorian chair"

class ModernTable(Table):       # Concrete product
    def eat_on(self):
        return "Eating on a modern table"

class VictorianTable(Table):        # Concrete product
    def eat_on(self):
        return "Eating on a Victorian table"

class FurnitureFactory(ABC):        # Abstract factory
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):     # Concrete factory 
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()

class VictorianFurnitureFactory(FurnitureFactory):      # Concrete factory
    def create_chair(self):
        return VictorianChair()

    def create_table(self):
        return VictorianTable()
    


