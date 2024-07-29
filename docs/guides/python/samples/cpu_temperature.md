# CPU Temperature

The CPU Temperature sample demonstrates how to use the on-chip Temperature sensor to measure the internal die temperature.

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
	import microcontroller

	while True:
		print((microcontroller.cpu.temperature,))
		time.sleep(0.1)
    ```

4. Your code will run as soon as the file is done saving. Click __Serial__ on Mu Editor's Top Menu to open a serial console. You should see the console output, similar to what is shown in the following:

    ``` { .bash .no-copy linenums="1"}
    Code stopped by auto-reload. Reloading soon.

    Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
    code.py output:
	(38.5484,)
	(38.5484,)
	(38.5484,)
	(39.1129,)
	(38.5484,)
	(38.5484,)
	(39.1129,)
	(39.1129,)
	(38.5484,)
	(39.1129,)
    ...
    ```

5. You can also use the plotter for data inspection. Click __Plotter__ on Mu Editor's Top Menu to open up a plotter pane:

    ![](../../../assets/images/mu-edittor-plotter-cputemp.png)


[Mu Editor]: ../getting-started.md#coding-with-mu-editor
[CircuitPython]: ../getting-started.md#installing-circuitpython
