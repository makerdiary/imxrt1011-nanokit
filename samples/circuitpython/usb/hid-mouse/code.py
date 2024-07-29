import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

left_button = digitalio.DigitalInOut(board.USR_BTN)
left_button.direction = digitalio.Direction.INPUT
left_button.pull = digitalio.Pull.DOWN

while True:
    if left_button.value is False:
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.2)  # Debounce delay
