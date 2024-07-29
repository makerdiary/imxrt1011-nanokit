# ADC

## Overview

This sample demonstrates how to use the ADC driver API. It reads ADC samples from all the available channels and prints the readings on the console. If voltage of the used reference can be obtained, the raw readings are converted to millivolts.

## Requirements

Before you start, check that you have the required hardware and software:

- 1x [iMX RT1011 Nano Kit](https://makerdiary.com/products/imxrt1011-nanokit)
- 1x USB-C Cable
- A computer running macOS, Linux, or Windows 7 or newer

## Building the sample

Before you start building, remember to [set up the environment](../setup.md) first.

Use the following steps to build the [ADC] sample on the command line.

1. Open a terminal window.

2. Go to `zephyrproject/imxrt1011-nanokit` directory created in the [Setting up the environment](../setup.md) section.

    ``` bash linenums="1"
    cd zephyrproject/imxrt1011-nanokit
    ```

3. Build the sample using the `west build` command, specifying the board (following the `-b` option) as `imxrt1011_nanokit`. To build the sample when working without the UF2 Bootloader, specify `-DEXTRA_CONF_FILE=overlay-nouf2.conf`.

    === "UF2 (default)"

        ``` bash linenums="1"
        west build -p always -b imxrt1011_nanokit samples/zephyr/adc
        ```
    
    === "No UF2"

        ``` bash linenums="1"
        west build -p always -b imxrt1011_nanokit samples/zephyr/adc -- -DEXTRA_CONF_FILE=overlay-nouf2.conf
        ```

    !!! Tip
        The `-p always` option forces a pristine build, and is recommended for new users. Users may also use the `-p auto` option, which will use heuristics to determine if a pristine build is required, such as when building another sample.

4. After running the `west build` command, the build files can be found in `build/zephyr`. 

## Flashing the firmware

The sample works with/without the UF2 Bootloader. The firmware can be found in `build/zephyr`.

To flash the firmware, complete the following steps:

=== "UF2 (default)"

    1. Plug your board into the USB port of your computer.
    2. Double-click the __RST__ button to enter UF2 Bootloader mode.
    3. The board will mount as a Mass Storage Device called __UF2BOOT__ and the Red LED blinks slow.
    4. Drag and drop `build/zephyr/zephyr.uf2` onto the __UF2BOOT__ volume. The RGB LED blinks red fast during flashing.
    5. Press __RST__ button on the board and the sample will start running.

=== "No UF2"
    
    1. Push and hold the __USR/BT__ button and plug your board into the USB port of your computer.
    2. Follow [Generating bootable image](../../../programming/mcuxpresso-secure-provisioning.md#generating-bootable-image) section to convert `build/zephyr/zephyr.hex` into a bootable image.
    3. Follow [Writing the bootable image](../../../programming/mcuxpresso-secure-provisioning.md#writing-the-bootable-image) section to flash the firmware.
    4. Press the __RST__ button on the board and the sample will start running.


## Testing

After flashing the firmware to your board, complete the following steps to test it:

1. Plug the board into the USB port of your computer.
2. Open up a serial terminal, specifying the correct serial port that your computer uses to communicate with the board:

    === "macOS/Linux"

        Open up a terminal and run:

        ``` bash linenums="1"
        screen <serial-port-name> 115200
        ```

    === "Windows"

        1. Start [PuTTY].
        2. Configure the correct serial port and click __Open__:

            ![](../../../assets/images/putty-settings.png)

3. Observe the output of the terminal. You should see the output, similar to what is shown in the following:

    ``` { .bash .no-copy linenums="1" }
    *** Booting Zephyr OS build v3.7.0-189-g988e4cf77094 ***
    ADC reading[0]:
    - adc@400c4000, channel 0: 118 = 95 mV
    - adc@400c4000, channel 1: 78 = 62 mV
    - adc@400c4000, channel 2: 85 = 68 mV
    - adc@400c4000, channel 3: 93 = 74 mV
    - adc@400c4000, channel 4: 90 = 72 mV
    - adc@400c4000, channel 5: 97 = 78 mV
    - adc@400c4000, channel 6: 91 = 73 mV
    - adc@400c4000, channel 7: 87 = 70 mV
    - adc@400c4000, channel 8: 3517 = 2833 mV
    - adc@400c4000, channel 9: 333 = 268 mV
    - adc@400c4000, channel 10: 3596 = 2897 mV
    - adc@400c4000, channel 11: 322 = 259 mV
    - adc@400c4000, channel 12: 84 = 67 mV
    - adc@400c4000, channel 13: 3640 = 2932 mV
    - adc@400c4000, channel 14: 3842 = 3095 mV
    ...
    ```

[ADC]: https://github.com/makerdiary/imxrt1011-nanokit/tree/main/samples/zephyr/adc
[PuTTY]: https://apps.microsoft.com/store/detail/putty/XPFNZKSKLBP7RJ