# Blinky

## Overview

The Blinky sample is a simple application which blinks an LED forever using the `digitalio` module. The source code shows how to configure the LED, then turn it on and off.

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
    import digitalio
    import board

    # Red LED
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    while True:
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)
    ```

4. Your code will run as soon as the file is done saving. Observe that the Red LED starts to blink.

[Mu Editor]: ../getting-started.md#coding-with-mu-editor
[CircuitPython]: ../getting-started.md#installing-circuitpython
