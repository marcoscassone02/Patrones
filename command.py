from abc import ABC, abstractmethod

class Command(ABC):     # Command interface
    @abstractmethod
    def execute(self):
        pass

class Light:        # Receiver
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")

class LightOnCommand(Command):      # Concrete command
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):     # Concrete command
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

class RemoteControl:        # Invoker
    def __init__(self):
        self._commands = {}

    def set_command(self, button, command: Command):
        self._commands[button] = command

    def press_button(self, button):
        if button in self._commands:
            self._commands[button].execute()
        else:
            print(f"No command assigned to button {button}")
