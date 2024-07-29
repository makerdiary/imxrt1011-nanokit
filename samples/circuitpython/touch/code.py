import time
import board
import touchio

touch_pad = board.A0  # Need a 1M resistor from the pin to ground

touch = touchio.TouchIn(touch_pad)

while True:
    if touch.value:
        print("Touched!")
    time.sleep(0.05)