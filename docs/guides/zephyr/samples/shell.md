# Shell

## Overview

The Shell sample shows you how to register custom commands into the Zephyr Shell. The following custom commands will be registered:

* __`bootloader`__: Enter the UF2 Bootloader at runtime.
* __`erase_app`__: Erase the entire application at runtime.

!!! Warning "Ensure UF2 Bootloader is present"
    This sample requires the UF2 Bootloader running on the board. If the UF2 Bootloader is not present or gets corrupted somehow, you can re-install the UF2 Bootloader by following the [UF2 Bootloader Installation](../../../programming/uf2boot.md#installing-uf2-bootloader) section.

## Requirements

Before you start, check that you have the required hardware and software:

- 1x [iMX RT1011 Nano Kit](https://makerdiary.com/products/imxrt1011-nanokit)
- 1x USB-C Cable
- A computer running macOS, Linux, or Windows 7 or newer

## Building the sample

Before you start building, remember to [set up the environment](../setup.md) first.

Use the following steps to build the [Shell] sample on the command line.

1. Open a terminal window.

2. Go to `zephyrproject/imxrt1011-nanokit` directory created in the [Setting up the environment](../setup.md) section.

    ``` bash linenums="1"
    cd zephyrproject/imxrt1011-nanokit
    ```

3. Build the sample using the `west build` command, specifying the board (following the `-b` option) as `imxrt1011_nanokit`.

    ``` bash linenums="1"
    west build -p always -b imxrt1011_nanokit samples/zephyr/shell
    ```

    !!! Tip
        The `-p always` option forces a pristine build, and is recommended for new users. Users may also use the `-p auto` option, which will use heuristics to determine if a pristine build is required, such as when building another sample.

4. After running the `west build` command, the build files can be found in `build/zephyr`. 

## Flashing the firmware

This sample should work with the UF2 Bootloader. The firmware can be found in `build/zephyr`.

To flash the firmware, complete the following steps:

1. Plug your board into the USB port of your computer.
2. Double-click the __RST__ button to enter UF2 Bootloader mode.
3. The board will mount as a Mass Storage Device called __UF2BOOT__ and the Red LED blinks slow.
4. Drag and drop `build/zephyr/zephyr.uf2` onto the __UF2BOOT__ volume. The RGB LED blinks red fast during flashing.
5. Press __RST__ button on the board and the sample will start running.

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

3. After connecting to the shell you should see the following output::

    ``` { .bash .no-copy linenums="1" }
    *** Booting Zephyr OS build v3.6.0-3959-gd0ae1a8b1057 ***


    uart:~$
    ```

4. The `bootloader` command can now be used:

    ``` { .bash .no-copy linenums="1" }
    uart:~$ bootloader
    Enter UF2 Bootloader...
    ```

    After this command is executed, the board will reset and run into the UF2 Bootloader mode.

5. Press __RST__ button to exit the UF2 Bootloader mode and run into the Shell application. Connect to the shell again.

6. The `erase_app` command can now be used:

    ``` { .bash .no-copy linenums="1" }
    uart:~$ erase_app
    Don't turn off the power! Erasing entire application...
    ```

    After this command is executed, the board will reset and start erasing the application memory. The Red LED will blink fast, and once erasing completed, the board will run in UF2 Bootloader mode as there is no application to boot.


[Shell]: https://github.com/makerdiary/imxrt1011-nanokit/tree/main/samples/zephyr/shell
[PuTTY]: https://apps.microsoft.com/store/detail/putty/XPFNZKSKLBP7RJ
