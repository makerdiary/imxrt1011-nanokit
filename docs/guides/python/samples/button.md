# Button

## Overview

The Button sample demonstrates the use of GPIO input using the `digitalio` module. It prints a message to the console each time the state of the button changes.

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
	
    ```

4. Your code will run as soon as the file is done saving. Click __Serial__ on Mu Editor's Top Menu to open a serial console. Observe the output of the console and press the __USR/BT__ button. You should see the output, similar to what is shown in the following:

    ``` { .bash .no-copy linenums="1"}
    Code stopped by auto-reload. Reloading soon.

    Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
    code.py output:
    Button is pressed
    Button is released
    Button is pressed
    Button is released
    ...
    ```

[Mu Editor]: ../getting-started.md#coding-with-mu-editor
[CircuitPython]: ../getting-started.md#installing-circuitpython
