from command import *

def main():
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()
    remote.set_command("on", light_on)
    remote.set_command("off", light_off)

    print("Pressing the 'on' button:")
    remote.press_button("on")

    print("Pressing the 'off' button:")
    remote.press_button("off")

    print("Pressing an unassigned button:")
    remote.press_button("up")

if __name__ == "__main__":
    main()

