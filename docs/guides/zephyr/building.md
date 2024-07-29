# Building and running the first sample

This guide explains how to build and run the first sample (for example, [Blinky]).

Before you start building, remember to [set up the environment](./setup.md) first.

## Build the Blinky sample

After completing the environment setup, use the following steps to build the [Blinky] sample on the command line.

1. Open a terminal window.

2. Go to `zephyrproject/imxrt1011-nanokit` directory created in the [Setting up the environment](./setup.md) section.

    ``` bash linenums="1"
    cd zephyrproject/imxrt1011-nanokit
    ```

3. Build the sample using the `west build` command, specifying the board (following the `-b` option) as `imxrt1011_nanokit`. To build the sample when working without the UF2 Bootloader, specify `-DEXTRA_CONF_FILE=overlay-nouf2.conf`.

    === "UF2 (default)"

        ``` bash linenums="1"
        west build -p always -b imxrt1011_nanokit samples/zephyr/blinky
        ```
    
    === "No UF2"

        ``` bash linenums="1"
        west build -p always -b imxrt1011_nanokit samples/zephyr/blinky -- -DEXTRA_CONF_FILE=overlay-nouf2.conf
        ```

    !!! Tip
        The `-p always` option forces a pristine build, and is recommended for new users. Users may also use the `-p auto` option, which will use heuristics to determine if a pristine build is required, such as when building another sample.

4. After running the `west build` command, the build files can be found in `build/zephyr`. 

## Flash and run the sample

The sample works with/without the UF2 Bootloader. The firmware can be found in `build/zephyr`.

To flash and run the firmware, complete the following steps:

=== "UF2 (default)"

    1. Plug your board into the USB port of your computer.
    2. Double-click the __RST__ button to enter UF2 Bootloader mode.
    3. The board will mount as a Mass Storage Device called __UF2BOOT__ and the Red LED blinks slow.
    4. Drag and drop `build/zephyr/zephyr.uf2` onto the __UF2BOOT__ volume. The RGB LED blinks red fast during flashing.
    5. Press the __RST__ button on the board and the Red LED will start to blink.
    6. Open up a serial terminal, specifying the correct serial port that your computer uses to communicate with the board.
    7. Observe the output of the terminal. You should see the output, similar to what is shown in the following:

        ``` { .bash .no-copy linenums="1" }
        *** Booting Zephyr OS build v3.7.0-189-g988e4cf77094 ***
        LED state: OFF
        LED state: ON
        LED state: OFF
        LED state: ON
        LED state: OFF
        LED state: ON
        ...
        ```

=== "No UF2"
    
    1. Push and hold the __USR/BT__ button and plug your board into the USB port of your computer.
    2. Follow [Generating bootable image](../../programming/mcuxpresso-secure-provisioning.md#generating-bootable-image) section to convert `build/zephyr/zephyr.hex` into a bootable image.
    3. Follow [Writing the bootable image](../../programming/mcuxpresso-secure-provisioning.md#writing-the-bootable-image) section to flash the firmware.
    4. Press the __RST__ button on the board and the Red LED will start to blink.
    5. Open up a serial terminal, specifying the correct serial port that your computer uses to communicate with the board.
    6. Observe the output of the terminal. You should see the output, similar to what is shown in the following:

        ``` { .bash .no-copy linenums="1" }
        *** Booting Zephyr OS build v3.7.0-189-g988e4cf77094 ***
        LED state: OFF
        LED state: ON
        LED state: OFF
        LED state: ON
        LED state: OFF
        LED state: ON
        ...
        ```

## Next steps

Explore more samples running on iMX RT1011 Nano Kit:

<div class="grid cards" markdown>

- __[Hello World](./samples/hello_world.md)__ – Print `Hello World` to the console over USB serial console
- __[Blinky](./samples/blinky.md)__ – Blink an LED forever using the GPIO API
- __[Button](./samples/button.md)__ – Demonstrate the use of GPIO input with interrupts
- __[ADC](./samples/adc.md)__ – Demonstrate the use of the ADC driver API
- __[PWM](./samples/pwm.md)__ – Demonstrate the use of the PWM driver API
- __[Shell](./samples/shell.md)__ – Demonstrate how to register custom commands into the Zephyr shell
- __[USB HID Keyboard](./samples/usb/hid_keyboard.md)__ – Demonstrate the HID Keyboard implementation
- __[USB HID Mouse](./samples/usb/hid_mouse.md)__ – Demonstrate the HID Mouse implementation

</div>

Zephyr also provide a variety of application samples and demos. Documentation for those is available in:

- [Zephyr's Samples and Demos](https://docs.zephyrproject.org/latest/samples/index.html#samples-and-demos)

[Blinky]: ./samples/blinky.md
