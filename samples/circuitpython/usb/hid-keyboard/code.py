import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# USR/BT button acts as A key on a keyboard
key_a = digitalio.DigitalInOut(board.USR_BTN)
key_a.direction = digitalio.Direction.INPUT
key_a.pull = digitalio.Pull.DOWN

# Red LED indicates A key is pressed
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

print("Waiting for key pin...")

while True:
    if not key_a.value:
        print("Key A pressed!")

        # Turn on Red LED
        led.value = True

        while not key_a.value:
            pass    # Wait for key A released

        # Type keycode `Shift+A`
        keyboard.press(Keycode.SHIFT, Keycode.A)
        keyboard.release_all()

        # Turn off Red LED
        led.value = False

    time.sleep(0.01)
