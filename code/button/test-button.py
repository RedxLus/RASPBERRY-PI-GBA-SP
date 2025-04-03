from gpiozero import Button
from signal import pause

# Configure the buttons and pins
gpio_pins = [5, 6, 13, 16, 17, 20, 22, 23, 24, 26, 27]
buttons = {pin: Button(pin, pull_up=True) for pin in gpio_pins}

def button_pressed(pin):
    print(f"Button on GPIO {pin} is being pressed!\n")

def button_released(pin):
    print(f"Button on GPIO {pin} is no longer pressed\n")

print("Available GPIO pins being monitored:", gpio_pins)
print("Press any button...\n")

for pin, button in buttons.items():
    button.when_pressed = lambda p=pin: button_pressed(p)
    button.when_released = lambda p=pin: button_released(p)

pause()