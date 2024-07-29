import time
import board
from analogio import AnalogIn

# Analog In 
analog_in = AnalogIn(board.A0)

# Convert ADC value to voltage in mV
def get_voltage(ain):
    return (ain.value * 3300) / 65536

while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
