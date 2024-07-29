/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/input/input.h>

#include <zephyr/usb/usb_device.h>
#include <zephyr/usb/usbd.h>
#include <zephyr/usb/class/usb_hid.h>

#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(main, LOG_LEVEL_INF);

#define REPORT_TYPE_INPUT	0x01
#define REPORT_TYPE_OUTPUT	0x02
#define REPORT_TYPE_FEATURE	0x03

#define OUTPUT_REPORT_MAX_LEN            1
#define OUTPUT_REPORT_BIT_MASK_CAPS_LOCK 0x02

static const uint8_t hid_report_desc[] = HID_KEYBOARD_REPORT_DESC();
static enum usb_dc_status_code usb_status;
static K_SEM_DEFINE(report_sem, 1, 1);

static const struct gpio_dt_spec kb_caps_led = 
	GPIO_DT_SPEC_GET_OR(DT_ALIAS(led0), gpios, {0});

enum kb_report_idx {
	KB_MOD_KEY = 0,
	KB_RESERVED,
	KB_KEY_CODE1,
	KB_KEY_CODE2,
	KB_KEY_CODE3,
	KB_KEY_CODE4,
	KB_KEY_CODE5,
	KB_KEY_CODE6,
	KB_REPORT_COUNT,
};

struct kb_event {
	uint16_t code;
	int32_t value;
};

K_MSGQ_DEFINE(kb_msgq, sizeof(struct kb_event), 2, 1);

static uint8_t __aligned(sizeof(void *)) report[KB_REPORT_COUNT];

static inline void status_cb(enum usb_dc_status_code status, const uint8_t *param)
{
	usb_status = status;
}

static ALWAYS_INLINE void rwup_if_suspended(void)
{
	if (IS_ENABLED(CONFIG_USB_DEVICE_REMOTE_WAKEUP)) {
		if (usb_status == USB_DC_SUSPEND) {
			usb_wakeup_request();
			return;
		}
	}
}

static void input_cb(struct input_event *evt)
{
	struct kb_event kb_evt;

	rwup_if_suspended();

	kb_evt.code = evt->code;
	kb_evt.value = evt->value;
	if (k_msgq_put(&kb_msgq, &kb_evt, K_NO_WAIT) != 0) {
		LOG_ERR("Failed to put new input event");
	}
}

INPUT_CALLBACK_DEFINE(NULL, input_cb);

static int kb_get_report(const struct device *dev,
			struct usb_setup_packet *setup, int32_t *len,
			uint8_t **data)
{
	LOG_INF("Unsupported get report");
	LOG_INF("bmRequestType: %02X bRequest: %02X wValue: %04X wIndex: %04X"
		" wLength: %04X", setup->bmRequestType, setup->bRequest,
		setup->wValue, setup->wIndex, setup->wLength);

	return 0;
}

static int kb_set_report(const struct device *dev,
			struct usb_setup_packet *setup, int32_t *len,
			uint8_t **data)
{
	uint8_t request_value[2];

	sys_put_le16(setup->wValue, request_value);

	switch (request_value[1]) {
	case REPORT_TYPE_OUTPUT:
		if (setup->wLength == OUTPUT_REPORT_MAX_LEN) {
			uint8_t report_val = ((**data) & OUTPUT_REPORT_BIT_MASK_CAPS_LOCK) ?
				1 : 0;
			(void)gpio_pin_set_dt(&kb_caps_led, report_val);
			return 0;
		}
		break;
	default:
		break;
	}

	LOG_INF("Unsupported set report");
	LOG_INF("bmRequestType: %02X bRequest: %02X wValue: %04X wIndex: %04X"
		" wLength: %04X", setup->bmRequestType, setup->bRequest,
		setup->wValue, setup->wIndex, setup->wLength);
	return 0;
}

static void kb_report_sent_cb(const struct device *dev)
{
	LOG_HEXDUMP_INF(report, sizeof(report), "Report sent:");
	k_sem_give(&report_sem);
}

static void kb_protocol_change(const struct device *dev, uint8_t protocol)
{
	LOG_INF("Protocol changed to %s",
		protocol == 0U ? "Boot Protocol" : "Report Protocol");
}

struct hid_ops kb_ops = {
	.get_report = kb_get_report,
	.set_report = kb_set_report,
	.int_in_ready = kb_report_sent_cb,
	.protocol_change = kb_protocol_change,
};

int main(void)
{
	const struct device *hid_dev;
	int ret;

	if (!gpio_is_ready_dt(&kb_caps_led)) {
		LOG_ERR("CAPS LOCK LED device %s is not ready", kb_caps_led.port->name);
		return -EIO;
	}

	ret = gpio_pin_configure_dt(&kb_caps_led, GPIO_OUTPUT_INACTIVE);
	if (ret != 0) {
		LOG_ERR("Failed to configure the LED pin, %d", ret);
		return -EIO;
	}

	hid_dev = device_get_binding("HID_0");

	if (hid_dev == NULL) {
		LOG_ERR("Cannot get USB HID Device");
		return 0;
	}

	usb_hid_register_device(hid_dev,
				hid_report_desc, sizeof(hid_report_desc),
				&kb_ops);

	usb_hid_init(hid_dev);

	ret = usb_enable(status_cb);

	LOG_INF("HID keyboard sample is initialized");

	while (true) {
		struct kb_event kb_evt;

		k_msgq_get(&kb_msgq, &kb_evt, K_FOREVER);

		switch (kb_evt.code) {
		case INPUT_KEY_0:
			if (kb_evt.value) {
				report[KB_KEY_CODE1] = HID_KEY_CAPSLOCK;
			} else {
				report[KB_KEY_CODE1] = 0;
			}

			break;
		default:
			LOG_INF("Unrecognized input code %u value %d",
				kb_evt.code, kb_evt.value);
			continue;
		}

		k_sem_take(&report_sem, K_FOREVER);

		ret = hid_int_ep_write(hid_dev, report, sizeof(report), NULL);
		if (ret) {
			LOG_ERR("HID write report error, %d", ret);
		}
	}

	return 0;
}
