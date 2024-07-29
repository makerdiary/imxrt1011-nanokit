# Setting up the environment

To start developing with the Zephyr RTOS, you should set up your development environment. This guide shows you how to set up a command-line Zephyr development environment on Ubuntu, macOS, or Windows manually.

For more details, please refer to the latest [Zephyr Project Documentation](https://docs.zephyrproject.org/latest/index.html)

## Select and Update OS

Install available updates for your operating system:

=== "Windows"

    Select __Start__ > __Settings__ > __Update & Security__ > __Windows Update__. Click __Check for updates__ and install any that are available.

=== "macOS"

    On macOS Mojave or later, select __System Preferences...__ > __Software Update__. Click __Update Now__ if necessary.

    On other versions, see [this Apple support topic](https://support.apple.com/en-us/HT201541).

=== "Ubuntu"

    This guide covers Ubuntu version 20.04 LTS and later.

    ``` bash linenums="1"
    sudo apt update
    ```

    ``` bash linenums="2"
    sudo apt upgrade
    ```

## Install dependencies

Next, you’ll install some host dependencies using your package manager.

The current minimum required version for the main dependencies are:

| Tool                  | Min. Version |
|-----------------------|--------------|
| [CMake]               | 3.20.5       |
| [Python]              | 3.10         |
| [Devicetree compiler] | 1.4.6        |

=== "Windows"

    We use [Chocolatey] to install dependencies here. If Chocolatey isn’t an option, you can install dependencies from their respective websites and ensure the command line tools added in your __`PATH`__ environment variable.


    1. [Install chocolatey](https://chocolatey.org/install).

    2. Open a `cmd.exe` window as __Administrator__. To do so, press the Windows key ++win++ , type `cmd.exe`, right-click the result, and choose __Run as Administrator__.

    3. Disable global confirmation to avoid having to confirm the installation of individual programs:

        ``` bash linenums="1"
        choco feature enable -n allowGlobalConfirmation
        ```

    4. Use `choco` to install the required dependencies:

        ``` bash linenums="1"
        choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
        ```

        ``` bash linenums="2"
        choco install ninja gperf python311 git dtc-msys2 wget unzip
        ```

    5. Close the window and open a new `cmd.exe` window __as a regular user__ to continue.

    !!! Tip
        To check the list of installed packages and their versions, run the following command:

        ``` bash linenums="1"
        choco list -lo
        ```

=== "macOS"

    1. Install [Homebrew]:

        ``` bash linenums="1"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```

    2. After the Homebrew installation script completes, follow the on-screen instructions to add the Homebrew installation to the path.

        * On macOS running on Apple Silicon, this is achieved with:

            ``` bash linenums="1"
            (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> ~/.zprofile
            ```

            ``` bash linenums="2"
            source ~/.zprofile
            ```

        * On macOS running on Intel, use the command for Apple Silicon, but replace `/opt/homebrew/` with `/usr/local/`.

    3. Use `brew` to install the required dependencies:

        ``` bash linenums="1"
        brew install cmake ninja gperf python3 ccache qemu dtc libmagic wget openocd
        ```

    4. Add the Homebrew Python folder to the path, in order to be able to execute `python` and `pip` as well `python3` and `pip3`.

        ``` bash linenums="1"
        (echo; echo 'export PATH="'$(brew --prefix)'/opt/python/libexec/bin:$PATH"') >> ~/.zprofile
        ```

        ``` bash linenums="2"
        source ~/.zprofile
        ```

    !!! Tip
        To check the versions of these dependencies installed, run the following command:

        ``` bash linenums="1"
        brew list --versions
        ```

=== "Ubuntu"

    1. If using an Ubuntu version older than 22.04, it is necessary to add extra repositories to meet the minimum required versions for the main dependencies listed above. In that case, download, inspect and execute the Kitware archive script to add the Kitware APT repository to your sources list. A detailed explanation of `kitware-archive.sh` can be found here [kitware third-party apt repository](https://apt.kitware.com/):

        ``` bash linenums="1"
        wget https://apt.kitware.com/kitware-archive.sh
        ```

        ``` bash linenums="2"
        sudo bash kitware-archive.sh
        ```
    
    2. Use `apt` to install the required dependencies:

        ``` bash linenums="1"
        sudo apt install --no-install-recommends git cmake ninja-build gperf \
        ccache dfu-util device-tree-compiler wget \
        python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file \
        make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
        ```
    
    3. Verify the versions of the main dependencies installed on your system by entering:

        ``` bash linenums="1"
        cmake --version
        ```

        ``` bash linenums="2"
        python3 --version
        ```

        ``` bash linenums="3"
        dtc --version
        ```

[CMake]: https://cmake.org/
[Python]: https://www.python.org/
[Devicetree compiler]: https://www.devicetree.org/
[Chocolatey]:https://chocolatey.org/
[Homebrew]: https://brew.sh/

## Get the code and install Python dependencies

To help you quickly build and run the samples on iMX RT1011 Nano Kit, the primary [imxrt1011-nanokit repository] contains the Zephyr manifest repositories, additional hardware drivers and tested samples, etc.

!!! Tip

    It is easy to run into Python package incompatibilities when installing dependencies at a system or user level. This situation can happen, for example, if working on multiple Zephyr versions or other projects using Python on the same machine.

    For this reason it is suggested to use [Python virtual environments](https://docs.python.org/3/library/venv.html).

=== "Windows"

    1. Open a `cmd.exe` terminal window __as a regular user__

    2. Change to `%HOMEPATH%` and create a workspace folder `zephyrproject` where all the required repositories will be cloned.

    3. Create a new virtual environment:

        ``` bat linenums="1"
        python -m venv zephyrproject\.venv
        ```

    4. Activate the virtual environment:

        ``` bat linenums="1"
        zephyrproject\.venv\Scripts\activate.bat
        ```

        Once activated your shell will be prefixed with `(.venv)`. The virtual environment can be deactivated at any time by running `deactivate`.

        !!! Note

            Remember to activate the virtual environment every time you start working.

    5. Install west:

        ``` bat linenums="1"
        pip install west
        ```

    6. Get the source code:

        ``` bat linenums="1"
        west init -m https://github.com/makerdiary/imxrt1011-nanokit --mr main zephyrproject
        ```

    7. Enter the following commands to clone the project repositories:

        ``` bat linenums="1"
        cd zephyrproject
        ```

        ``` bat linenums="2"
        west update
        ```

        After all the repositories updated, your workspace folder now looks similar to this:

        ``` { .bat .no-copy linenums="1" }
        zephyrproject
        |___ .west
        |___ imxrt1011-nanokit
        |___ modules
        |___ zephyr
        |___ ...

        ``` 

    8. Export a [Zephyr CMake package]. This allows CMake to automatically load boilerplate code required for building Zephyr applications.

        ``` bat linenums="1"
        west zephyr-export
        ```

    9. Zephyr’s `scripts\requirements.txt` file declares additional Python dependencies. Install them with `pip`.

        ``` bat linenums="1"
        pip install -r %HOMEPATH%\zephyrproject\zephyr\scripts\requirements.txt
        ```

=== "macOS"

    1. Open up a terminal window.
    2. Change to `~` and create a workspace folder `zephyrproject` where all the required repositories will be cloned.
    3. Create a new virtual environment:

        ``` sh linenums="1"
        python3 -m venv ~/zephyrproject/.venv
        ```

    4. Activate the virtual environment:

        ``` sh linenums="1"
        source ~/zephyrproject/.venv/bin/activate
        ```

        Once activated your shell will be prefixed with `(.venv)`. The virtual environment can be deactivated at any time by running `deactivate`.

        !!! Note

            Remember to activate the virtual environment every time you start working.

    5. Install west:

        ``` sh linenums="1"
        pip install west
        ```

    6. Get the source code:

        ``` sh linenums="1"
        west init -m https://github.com/makerdiary/imxrt1011-nanokit --mr main zephyrproject
        ```

    7. Enter the following commands to clone the project repositories:

        ``` sh linenums="1"
        cd zephyrproject
        ```

        ``` sh linenums="2"
        west update
        ```

        After all the repositories updated, your workspace folder now looks similar to this:

        ``` { .sh .no-copy linenums="1" }
        zephyrproject
        |___ .west
        |___ imxrt1011-nanokit
        |___ modules
        |___ zephyr
        |___ ...

        ``` 

    8. Export a [Zephyr CMake package]. This allows CMake to automatically load boilerplate code required for building Zephyr applications.

        ``` sh linenums="1"
        west zephyr-export
        ```

    9. Zephyr’s `scripts\requirements.txt` file declares additional Python dependencies. Install them with `pip`.

        ``` sh linenums="1"
        pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
        ```

=== "Ubuntu"

    1. Open up a terminal window.
    2. Change to `~` and create a workspace folder `zephyrproject` where all the required repositories will be cloned.
    3. Use `apt` to install Python `venv` package:

        ``` sh linenums="1"
        sudo apt install python3-venv
        ```

    4. Create a new virtual environment:

        ``` sh linenums="1"
        python3 -m venv ~/zephyrproject/.venv
        ```

    5. Activate the virtual environment:

        ``` sh linenums="1"
        source ~/zephyrproject/.venv/bin/activate
        ```

        Once activated your shell will be prefixed with `(.venv)`. The virtual environment can be deactivated at any time by running `deactivate`.

        !!! Note

            Remember to activate the virtual environment every time you start working.

    6. Install west:

        ``` sh linenums="1"
        pip install west
        ```

    7. Get the source code:

        ``` sh linenums="1"
        west init -m https://github.com/makerdiary/imxrt1011-nanokit --mr main zephyrproject
        ```

    8. Enter the following commands to clone the project repositories:

        ``` sh linenums="1"
        cd zephyrproject
        ```

        ``` sh linenums="2"
        west update
        ```

        After all the repositories updated, your workspace folder now looks similar to this:

        ``` { .sh .no-copy linenums="1" }
        zephyrproject
        |___ .west
        |___ imxrt1011-nanokit
        |___ modules
        |___ zephyr
        |___ ...

        ``` 

    9. Export a [Zephyr CMake package]. This allows CMake to automatically load boilerplate code required for building Zephyr applications.

        ``` sh linenums="1"
        west zephyr-export
        ```

    10. Zephyr’s `scripts\requirements.txt` file declares additional Python dependencies. Install them with `pip`.

        ``` sh linenums="1"
        pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
        ```

[imxrt1011-nanokit repository]: https://github.com/makerdiary/imxrt1011-nanokit
[Zephyr CMake package]: https://docs.zephyrproject.org/latest/build/zephyr_cmake_package.html#cmake-pkg

## Install the Zephyr SDK

The [Zephyr Software Development Kit (SDK)] contains toolchains for each of Zephyr’s supported architectures, which include a compiler, assembler, linker and other programs required to build Zephyr applications.

It also contains additional host tools, such as custom QEMU and OpenOCD builds that are used to emulate, flash and debug Zephyr applications.

=== "Windows"

    1. Open a `cmd.exe` terminal window __as a regular user__.
    2. Download the [Zephyr SDK bundle]:

        ``` bat linenums="1"
        cd %HOMEPATH%
        ```

        ``` bash linenums="2"
        wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5-1/zephyr-sdk-0.16.5-1_windows-x86_64.7z
        ```

    3. Extract the Zephyr SDK bundle archive:

        ``` bat linenums="1"
        7z x zephyr-sdk-0.16.5-1_windows-x86_64.7z
        ```
    
        !!! Note
            It is recommended to extract the Zephyr SDK bundle at one of the following locations:

            - `%HOMEPATH%`
            - `%PROGRAMFILES%`

            The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>` directory and, when extracted under `%HOMEPATH%`, the resulting installation path will be `%HOMEPATH%\zephyr-sdk-<version>`.

    4. Run the Zephyr SDK bundle setup script:

        ``` bat linenums="1"
        cd zephyr-sdk-0.16.5-1
        ```

        ``` bat linenums="2"
        setup.cmd
        ```

        !!! Note
            You only need to run the setup script once after extracting the Zephyr SDK bundle.
            
            You must rerun the setup script if you relocate the Zephyr SDK bundle directory after the initial setup.

=== "macOS"

    1. Download and verify the [Zephyr SDK bundle]:

        ``` bash linenums="1"
        cd ~
        ```

        ``` bash linenums="2"
        curl -L -O https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5-1/zephyr-sdk-0.16.5-1_macos-x86_64.tar.xz
        ```

        ``` bash linenums="3"
        curl -L https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5-1/sha256.sum | shasum --check --ignore-missing
        ```

        If your host architecture is 64-bit ARM (Apple Silicon, also known as M1), replace `x86_64` with `aarch64` in order to download the 64-bit ARM macOS SDK.

    2. Extract the Zephyr SDK bundle archive:

        ``` bash linenums="1"
        tar xvf zephyr-sdk-0.16.5-1_macos-x86_64.tar.xz
        ```

        !!! Note
            It is recommended to extract the Zephyr SDK bundle at one of the following locations:

            - `$HOME`
            - `$HOME/.local`
            - `$HOME/.local/opt`
            - `$HOME/bin`
            - `/opt`
            - `/usr/local`

            The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>` directory and, when extracted under `$HOME`, the resulting installation path will be `$HOME/zephyr-sdk-<version>`.

    3. Run the Zephyr SDK bundle setup script:

        ``` bash linenums="1"
        cd zephyr-sdk-0.16.5-1
        ```

        ``` bash linenums="2"
        ./setup.sh
        ```

        !!! Note
            You only need to run the setup script once after extracting the Zephyr SDK bundle.

            You must rerun the setup script if you relocate the Zephyr SDK bundle directory after the initial setup.

=== "Ubuntu"

    1. Download and verify the [Zephyr SDK bundle]:

        ``` bash linenums="1"
        cd ~
        ```

        ``` bash linenums="2"
        wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5-1/zephyr-sdk-0.16.5-1_linux-x86_64.tar.xz
        ```

        ``` bash linenums="3"
        wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5-1/sha256.sum | shasum --check --ignore-missing
        ```

        If your host architecture is 64-bit ARM (for example, Raspberry Pi), replace `x86_64` with `aarch64` in order to download the 64-bit ARM Linux SDK.


    2. Extract the Zephyr SDK bundle archive:

        ``` bash linenums="1"
        tar xvf zephyr-sdk-0.16.5-1_linux-x86_64.tar.xz
        ```

        !!! Note
            It is recommended to extract the Zephyr SDK bundle at one of the following locations:

            - `$HOME`
            - `$HOME/.local`
            - `$HOME/.local/opt`
            - `$HOME/bin`
            - `/opt`
            - `/usr/local`

            The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>` directory and, when extracted under `$HOME`, the resulting installation path will be `$HOME/zephyr-sdk-<version>`.

    3. Run the Zephyr SDK bundle setup script:

        ``` bash linenums="1"
        cd zephyr-sdk-0.16.5-1
        ```

        ``` bash linenums="2"
        ./setup.sh
        ```

        !!! Note
            You only need to run the setup script once after extracting the Zephyr SDK bundle.
            
            You must rerun the setup script if you relocate the Zephyr SDK bundle directory after the initial setup.

    4. Install [udev] rules, which allow you to flash most Zephyr boards as a regular user:

        ``` bash linenums="1"
        sudo cp ~/zephyr-sdk-0.16.5-1/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d
        ```

        ``` bash linenums="2"
        sudo udevadm control --reload
        ```

[Zephyr Software Development Kit (SDK)]: https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html#toolchain-zephyr-sdk
[Zephyr SDK bundle]: https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.5-1
[udev]: https://en.wikipedia.org/wiki/Udev