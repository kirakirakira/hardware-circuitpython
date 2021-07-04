# Script to go with slides

## 1. Title

Welcome to Basics of Hardware with a PyRuler! My name is Kira Hartlage, and I will be teaching you a bit about hardware and how you can get started using Python.

## 2. Introduction

My name is Kira Hartlage. I have a background in mechanical engineering and consumer appliance part design at GE Appliances. I started my software journey teaching myself Python using EdX, Coursera, and other online courses before branching out and switching to embedded development at my current company where now I write code for microcontrollers that are on our consumer appliances.

## 2. Desired Outcomes

Here are our desired outcomes for our time together. I’ll introduce to you a bit about embedded firmware development. I’ll introduce how you can use CircuitPython as an alternative to C, which is the most common software language used for writing embedded software. We’ll look at an example of how to write code for hardware using the PyRuler. Then I’ll show you resources and examples of projects that you can explore to learn on your own.

## 5. Embedded systems

We will start with what is embedded firmware or is it embedded software or maybe embedded systems?

Embedded software development is basically writing code to control a device that is not a computer. So you typically don’t have an operating system, and you will be dealing with memory and time constraints for the particular device that you’re writing code for. Embedded software can also be called firmware as firmware is stored in non-volatile memory such as ROM, Flash, or EEPROM. In the past, you would not be able to update the device’s non-volatile memory, hence it was firm. But nowadays there are methods to update non-volatile memory without too much headache.

## 6. Hardware - Microcontrollers

Microcontrollers are an integrated circuit with a processor, memory, and various input/output peripherals. Microcontrollers have 3 main pieces: instructions which is what the microcontroller is capable of doing, registers which are fast storage locations in memory that the microcontroller has that the instructions can use, and it also has other memory which can be used to store your code and data, but they are slower for the microcontroller to access than the registers.

## 7. Hardware - Peripherals

Peripherals are the various parts of the microcontroller that interface with the outside world. Some examples are:
1. GPIOs (General Purpose Input/Output) - examples for this would be lighting an LED, reading a binary sensor input
1. ADC (Analog to Digital Control) - example would be reading a thermistor for room temperature
1. DAC (Digital to Analog Control) - example would be video or audio converters from digital to analog signals
1. PWM (Pulse-width modulation) - example would be controlling a variable speed motor
1. Hardware timers
1. Serial communication - UART, I2C, SPI - these are used to communication between two devices such as microcontroller to microcontroller or sensor to microcontroller
1. Interrupts - an interrupt is a signal to the microcontroller that's emitted by hardware or software to indicate that an event has happened and needs immediate attention; example is pressing a key on a keyboard or clicking a mouse - this causes a hardware interrupt that will be serviced by the processor to read the key or mouse click and act correspondingly


## 8. CircuitPython

https://github.com/adafruit/circuitpython
https://circuitpython.org/
Example guides: https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/CircuitPython_Essentials

Commonly, C is the language of choice for writing code for microcontrollers. C is a compiled, low-level language that plays nicely with low-level hardware needs as it can be very efficient. It's also smaller in memory as it doesn't rely on as many libraries as our higher-level languages, and microcontrollers are very memory-constrained. C is a bit more difficult to learn than other languages and it can be difficult to get a microcontroller started up. But if you're looking to get into hardware, thankfully Adafruit has created a derivative of MicroPython (which is a full Python compiler and runtime that runs on bare-metal) known as CircuitPython to specifically to educate people on how to program microcontrollers and get up and going as quickly as possible.

There are many low-cost microcontroller boards, and with CircuitPython there are no special desktop software requirements. You can use any text editor to start editing code. You won’t need to install a fancy compiler or need any special equipment to upload the code either to the board. Since CircuitPython is based on Python, it’s also easy to transition and get started with little prior programming experience.

The CircuitPython code lives on the board itself, and there's a serial console and REPL that you can set up to get live feedback and interact with the hardware. There are many libraries and drivers available as well already from Adafruit for various sensors, components, and boards so you don’t have to write your own from scratch.

## 9. PyRuler

The PyRuler is a ruler...and it’s a reference board that shows you what various PCB (printed circuit board) components look like, their name and their size. But it also has a few cool features that makes it a simple board to get started with in your CircuitPython journey.

It has a Trinket M0 (a Cortex M0 microcontroller), as well as 4 capacitive touch pads with matching LEDs. It comes with code already loaded it on, so all you need to do is plug and play. Each of 3 of the capacitive touch buttons will press a Greek symbol as keyboard input on your computer.

Because the code is already there, it makes it easy to edit and change what is printed. I modified the example code to print what I wanted.

## 12. PyRuler Project #1
I also found someone else's project that turned the PyRuler into a panic button for when you need to mute yourself during a conference call.

I added a toggle for the video, toggle for the mute button, and added a shortcut to go to search within Teams. If you press the Digi-Key button, it prints "LGTM :+1:", which is what we like to type on each other's pull requests at work.

<Muting conference call and turning on/off camera>

## 13. Circuit Playground Express/Bluefruit
https://learn.adafruit.com/adafruit-circuit-playground-express
https://www.adafruit.com/product/4333

## 14. Circuit Playground Express/Bluefruit Project #2
Scheduling blinking lights

## 15. Circuit Playground Express/Bluefruit Project #3
Playing music with buttons, turn on/off light with switch

## 15. Resources

## 16. Thank you