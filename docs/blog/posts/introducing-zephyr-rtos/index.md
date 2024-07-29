---
title: Introducing Zephyr RTOS
date: 2024-06-16
authors:
  - makerdiary
cover: cover.png
description: >
  Zephyr RTOS is an open-source collaborative effort uniting developers and users in building a best-in-class small,
  scalable real⁃time operating system.
---

# Introducing Zephyr RTOS

## What Is Zephyr?

[The Zephyr™ Project] is a scalable RTOS, which supports multiple hardware architectures, optimized for resource-constrained devices, and built with security in mind. It is based on a small-footprint kernel designed for use on
resource-constrained systems.

[NXP], as one of the six founding member of [The Zephyr™ Project], actively contributes to the Zephyr community. All the i.MX RT crossover MCUs have support in the Zephyr source tree which are actively maintained. Developers are able
to tailor a solution easily to meet their needs using a true open source project with hardware, developer tools, and sensor and device drivers. Security enhancements with Zephyr OS enable easy implementation of device management, connectivity stacks, and file systems.

For more details on the Zephyr RTOS, visit www.zephyrproject.org/.

## Key Features of Zephyr

Zephyr has several important features that contribute to its real-time development appeal and its adoption in embedded systems and connected devices:

* __Open source__: Zephyr is an open source project that promotes collaboration and allows developers to freely access, modify, and contribute code.
* __Modular architecture__: Zephyr’s modular architecture gives developers the flexibility to select and include only what is necessary from existing Zephyr components or to develop and include new components to create an optimized footprint for built-for-purpose RTOS implementation.
* __Scalability__: Zephyr is scalable across a wide range of devices with different hardware capabilities, from small sensor nodes to powerful IoT gateways.
* __Cross-architecture support__: Zephyr has broad hardware support that includes various architectures, such as Arm, x86, and RISC-V, making it compatible with a spectrum of hardware platforms. This simplifies development and promotes interoperability.
* __Real-time capabilities__: Zephyr provides real-time capabilities to applications that require the precise timing and responsiveness often necessary in industrial automation, healthcare, and automotive use cases.
* __Libraries and protocols__: The Zephyr Project includes a comprehensive set of libraries, protocols, and device drivers. These resources simplify development, enabling developers to build real-time and embedded applications without having to start from scratch.
* __Security focus__: Zephyr provides features such as memory protection, access controls, and secure boot options. This focus on security is crucial for embedded applications that demand data integrity and user privacy.
* __Community support__: Zephyr is supported by a growing and active community of developers and contributors with real-time and embedded systems expertise.

## Get Involved

We think the best way to learn is by doing. An extensive set of guides are available to take you through the basics of Zephyr application development on iMX RT1011 Nano Kit.

<div class="grid cards" markdown>

-   __Setting up the environment__

    ---

    Learn how to set up a command-line Zephyr development environment.

    [:octicons-arrow-right-24: Learn more](../../../guides/zephyr/setup.md)

-   __Building and running the first sample__

    ---

    Learn how to build and run the first sample Blinky.

    [:octicons-arrow-right-24: Learn more](../../../guides/zephyr/building.md)

-   __More samples__

    ---

    Explore more samples running on iMX RT1011 Nano Kit.

    [:octicons-arrow-right-24: Explore more](../../../guides/zephyr/samples/index.md)

</div>



[The Zephyr™ Project]: https://www.zephyrproject.org/
[NXP]: https://www.nxp.com/
