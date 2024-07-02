class Computer:     # Product
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.cpu = None
        self.gpu = None
        self.memory = None
        self.storage = None
        self.screen_size = None

    def __str__(self):
        return f"Serial Number: {self.serial_number}\nCPU: {self.cpu}\nGPU: {self.gpu}\nMemory: {self.memory}\nStorage: {self.storage}\nScreen Size: {self.screen_size}"

class ComputerBuilder:      # Builder
    def __init__(self, serial_number):
        self.computer = Computer(serial_number)

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_screen_size(self, screen_size):
        self.computer.screen_size = screen_size
        return self

    def get_computer(self):
        return self.computer

class Director:     # Director
    def construct_gaming_computer(self, builder):
        return builder.set_cpu("Intel i7") \
                      .set_gpu("Nvidia RTX 3080") \
                      .set_memory("16GB DDR4") \
                      .set_storage("1TB SSD") \
                      .set_screen_size("27-inch") \
                      .get_computer()

    def construct_office_computer(self, builder):
        return builder.set_cpu("Intel i5") \
                      .set_gpu("Integrated GPU") \
                      .set_memory("8GB DDR4") \
                      .set_storage("512GB SSD") \
                      .set_screen_size("24-inch") \
                      .get_computer()

