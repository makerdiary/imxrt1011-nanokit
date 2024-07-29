/*
 * Copyright (c) 2012-2014 Wind River Systems, Inc.
 * Copyright (c) 2016-2024 Makerdiary <https://makerdiary.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <stdio.h>

int main(void)
{
	while (1) {
		printf("Hello World! %s\n", CONFIG_BOARD_TARGET);
		k_sleep(K_SECONDS(1));
	}

	return 0;
}
