# Copyright (c) 2016-2024 Makerdiary <https://makerdiary.com>
# SPDX-License-Identifier: Apache-2.0

board_runner_args(uf2 "--board-id=IMXRT1011-NANO-KIT-RevA")
board_runner_args(pyocd "--target=mimxrt1010")
board_runner_args(jlink "--device=MIMXRT1011")
include(${ZEPHYR_BASE}/boards/common/uf2.board.cmake)
include(${ZEPHYR_BASE}/boards/common/pyocd.board.cmake)
include(${ZEPHYR_BASE}/boards/common/jlink.board.cmake)
