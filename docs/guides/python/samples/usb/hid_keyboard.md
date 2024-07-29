# USB HID Keyboard

## Overview

The USB HID Keyboard sample demonstrates using the USB Human Interface Device (HID) module to implement a keyboard input device that you can connect to your computer.

This sample code enumerates the iMX RT1011 Nano Kit into a HID keyboard that has an <kbd>A</kbd> key connected to the __USR/BT__ button.

!!! Tip
    `adafruit_hid` is pre-built into [CircuitPython] as a frozen module, so that it can be imported in the code directly.

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
    ```

4. Your code will run as soon as the file is done saving. The board will enumerate as a HID keyboard. Click __Serial__ on Mu Editor's Top Menu to open a serial console. You should see the console output, similar to what is shown in the following:

    ``` { .bash .no-copy linenums="1"}
    Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
    code.py output:
    Waiting for key pin...
    ```

5. Open a text editor and press __USR/BT__ button on the board. Every button press sends a character __`A`__ to the computer, and this will be displayed in the text editor.

[Mu Editor]: ../../getting-started.md#coding-with-mu-editor
[CircuitPython]: ../../getting-started.md#installing-circuitpython
