# PWM

## Overview

The PWM sample demonstrates using the `pwmio` module to fade the __Red LED__ (alias __`LED`__) on iMX RT1011 Nano Kit.

## Requirements

Before you start, check that you have the required hardware and software:

- 1x [iMX RT1011 Nano Kit](https://makerdiary.com/products/imxrt1011-nanokit) running the [CircuitPython] firmware
- 1x USB-C Cable
- [Mu Editor]
- A computer running macOS, Linux, or Windows 7 or newer

## Running the code

To run the code, complete the following steps:

1. Connect iMX RT1011 Nano Kit to your computer using the USB-C Cable.
2. Start Mu Editor, click __Load__ to open `code.py` in the __CIRCUITPY__ drive.
3. Copy and paste the following code into `code.py` and click __Save__:

    ``` python linenums="1" title="CIRCUITPY/code.py"
	import time
	import board
	import pwmio

	# Connect LED to PWMOut
	led = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)

	while True:
		for i in range(100):
			# PWM LED up and down
			if i < 50:
				led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
			else:
				led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
			time.sleep(0.01)
    ```

4. Your code will run as soon as the file is done saving. Observe that the Red LED starts off increases its brightness until it is fully on and then decreases until the LED is off, completing on fade cycle.

[Mu Editor]: ../getting-started.md#coding-with-mu-editor
[CircuitPython]: ../getting-started.md#installing-circuitpython
