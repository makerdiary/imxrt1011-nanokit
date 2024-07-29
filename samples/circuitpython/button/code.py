import board
import digitalio

# User Button
button = digitalio.DigitalInOut(board.USR_BTN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

last_value = button.value

while True:
    if last_value != button.value:
        last_value = button.value
        print('Button is ' + ('released' if button.value else 'pressed'))
