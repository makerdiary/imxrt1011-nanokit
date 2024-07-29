#
# Copyright (c) 2016-2024 Makerdiary <https://makerdiary.com>
#
# SPDX-License-Identifier: Apache-2.0
#

zephyr_library()

# Library may be empty due to kconfigs
zephyr_library_property(ALLOW_EMPTY TRUE)

if(CONFIG_NXP_IMXRT_BOOT_HEADER)
  zephyr_compile_definitions(XIP_BOOT_HEADER_ENABLE=1)
  zephyr_compile_definitions(BOARD_FLASH_SIZE=CONFIG_FLASH_SIZE*1024)
  zephyr_library_sources(flexspi_nor_config.c)
endif()

if(CONFIG_MCUX_GPT_TIMER)
  message(WARNING "You appear to be using the GPT hardware timer. "
    "This timer will enable lower power modes, but at the cost of reduced "
    "hardware timer resolution")
endif()
