/*
 * Copyright (c) 2016-2024 Makerdiary <https://makerdiary.com>
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/shell/shell.h>

#define DBL_TAP_MAGIC            0xf01669ef /* Enter DFU magic */
#define DBL_TAP_MAGIC_QUICK_BOOT 0xf02669ef /* Skip double tap delay detection */
#define DBL_TAP_MAGIC_ERASE_APP  0xf5e80ab4 /* Erase entire application !! */

int main(void)
{
	return 0;
};

static int cmd_bootloader(const struct shell *sh, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);


	SNVS->LPGPR[3] = DBL_TAP_MAGIC;

	shell_print(sh, "Enter UF2 Bootloader...");

	NVIC_SystemReset();

	return 0;
}

static int cmd_erase_app(const struct shell *sh, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);


	SNVS->LPGPR[3] = DBL_TAP_MAGIC_ERASE_APP;

	shell_print(sh, "Don't turn off the power! Erasing entire application...");

	NVIC_SystemReset();

	return 0;
}

SHELL_CMD_ARG_REGISTER(bootloader, NULL, "Enter UF2 Bootloader", cmd_bootloader, 1, 0);
SHELL_CMD_ARG_REGISTER(erase_app, NULL, "Erase entire application", cmd_erase_app, 1, 0);
