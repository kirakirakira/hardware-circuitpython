# Script to go with slides

## 1. Title

Welcome to Basics of Hardware with a PyRuler! My name is Kira Hartlage, and I will be teaching you a bit about hardware and how you can get started using Python.

## 2. Introduction

My name is Kira Hartlage. I have a background in mechanical engineering and consumer appliance part design at GE Appliances. I started my software journey teaching myself Python using EdX, Coursera, and other online courses before branching out and switching to embedded development at my current company where now I write code for microcontrollers that are on our consumer appliances.

## 3. Desired Outcomes

Here are our desired outcomes for our time together. I’ll introduce to you a bit about embedded firmware development. I’ll introduce how you can use CircuitPython as an alternative to C, which is the most common software language used for writing embedded software. We’ll look at an example of how to write code for hardware using the PyRuler. Then I’ll show you resources and examples of projects that you can explore to learn on your own.

## 4. Embedded systems

We will start with what is embedded firmware or is it embedded software or maybe embedded systems?

Embedded software development is basically writing code to control a device that is not a computer. So you typically don’t have an operating system, and you will be dealing with memory and time constraints for the particular device that you’re writing code for. Embedded software can also be called firmware as firmware is stored in non-volatile memory such as ROM, Flash, or EEPROM. In the past, you would not be able to update the device’s non-volatile memory, hence it was firm. But nowadays there are methods to update non-volatile memory without too much headache.

## 5. Hardware

Central to many hardware applications is the microcontroller. It is an integrated circuit with a processor, memory, and various input/output peripherals. Microcontrollers are designed for embedded systems, whereas microprocessors are used in personal computers and other general purpose applications.

Peripherals are the various parts of the microcontroller that interface with the outside world.

## 6. Hardware - Microcontrollers

Microcontrollers have 3 main pieces:
1. Instructions - what the microcontroller is capable of doing
2. Registers - which are fast storage locations in memory that the microcontroller has that the instructions can use
3. Other memory - which can be used to store your code and data, but they are slower for the microcontroller to access than it is to access the registers

## 7. Hardware - Peripherals

Some examples of peripherals are:
1. GPIOs (General Purpose Input/Output) - examples for this would be output to light an LED or reading a binary sensor input such as if a magnet passed over a hall effect sensor or not
1. ADC (Analog to Digital Control) - example would be reading a thermistor for room temperature where the input is an analog count and you would translate that to a meaningful temperature
1. DAC (Digital to Analog Control) - example would be video or audio converters that translate from digital to analog signals
1. PWM (Pulse-width modulation) - example would be controlling a variable speed motor with a pulse-width signal with varying frequency and/or duty-cycle
1. Hardware timers to keep time or count operations or events
1. Serial communication - UART, I2C, SPI - these are used to communication between two devices such as microcontroller to microcontroller or sensor to microcontroller
1. Interrupts - an interrupt is a signal to the microcontroller that's emitted by hardware or software to indicate that an event has happened and needs immediate attention; example is pressing a key on a keyboard or clicking a mouse - this causes a hardware interrupt that will be serviced by the processor to read the key or mouse click and act accordingly

## 8. CircuitPython

https://github.com/adafruit/circuitpython
https://circuitpython.org/
Example guides: https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/CircuitPython_Essentials

Commonly, C is the language of choice for writing code for microcontrollers. C is a compiled, low-level language that plays nicely with low-level hardware needs as it can be very small in size and efficient. It's small in terms of memory because it doesn't rely on as many libraries as higher-level languages do, and microcontrollers are very memory-constrained. C is a bit more difficult to learn than other languages and it can be difficult to get a microcontroller started up from scratch. But if you're looking to get into hardware, thankfully Adafruit has created a derivative of MicroPython (which is a full Python compiler and runtime environment that runs on bare-metal) known as CircuitPython. They created CircuitPython specifically to educate people on how to program microcontrollers and get up and going as quickly as possible.

There are many low-cost microcontroller boards, and with CircuitPython there are no special desktop software requirements. You can use any text editor to start editing code. You won’t need to install a fancy compiler or need any special equipment to upload the code either to the board. Since CircuitPython is based on Python, it’s also easy to transition and get started with little prior programming experience.

## 9. File Structure and Serial Console

The CircuitPython code lives on the board itself, and there's a serial console and REPL that you can set up to get live feedback and interact with the hardware. There are many libraries and drivers available as well already from Adafruit for various sensors, components, and boards so you don’t have to write your own from scratch.

When you plug in a board via USB that already has CircuitPython loaded, you'll see it pop up as an external USB device. If you look inside the folder, you'll see it's contents. Here is an example of what you would see if for the first time plugging in a PyRuler.

Instructions for connecting the serial console and REPL can be found on Adafruit's website. But here is what it looks like.

## 10. PyRuler

The PyRuler is a ruler...and it’s a reference board that shows you what various PCB (printed circuit board) components look like, their name and their size. But it also has a few cool features that makes it a simple board to get started with in your CircuitPython journey.

It has a Trinket M0 (a Cortex M0 microcontroller), as well as 4 capacitive touch pads with matching LEDs. It comes with code already loaded on it, so all you need to do is plug and play. Each of the 3 capacitive touch buttons will type a Greek symbol as keyboard input on your computer.

Because the code is already there on the PyRuler, it makes it easy to edit and change what is printed. I modified the example code to print what I wanted.

## 11. PyRuler Project #1

If you press the Digi-Key button, it prints "LGTM :+1:", which is what we like to type on each other's pull requests at work.

I also found someone else's project that turned the PyRuler into a panic button for when you need to mute yourself during a conference call. I added a toggle for the video camera, toggle for the mute button, and added a shortcut to go to search within Microsoft Teams by modifying the existing code on the PyRuler and looking up what the keyboard shortcuts are for these. More details on how the code works is included in the Appendix which is in my Github repo.

## 12. Circuit Playground Express/Bluefruit

Another intro boards that are available from Adafruit with CircuitPython on them are the Circuit Playground Express and Circuit Playground Bluefruit which is the Express plus Bluetooth capability. It has many more sensors built in on the board than the PyRuler does.

https://learn.adafruit.com/adafruit-circuit-playground-express
https://www.adafruit.com/product/4333

## 13. Circuit Playground Express/Bluefruit Project #2
Playing music with buttons, turn on/off light with switch

In this example, I am lighting up the LEDs if the sound sensor measures sound over a threshold of 250. I am actually banging on the table to make noise in this case.

Also, if you press the A button, it'll play the radio tune mp3 that's loaded on to the board, and if you press the B button, it'll play the pump tune mp3.

With the sound sensor, you can also change which LEDs light up or gradually increase the brightness the louder the sound. That is one of the example projects that you can find in Adafruit's Github repo for these boards. They provide lots of examples to get you going, so you can combine things as you like.

## 14. Circuit Playground Express/Bluefruit Project #3
The last project I'll show you is an example of multi-tasking or scheduling as this is non-trivial on a microcontroller. You have one thread of operation and everything is operating in the one main loop. So one way to do multiple things at once is to use a software timer and have it running, and then handle events asynchronously.

This example blinks multiple LEDs at different rates. To do this there is one software timer running. At start-up, each LED is set up with a defined interval at which it should blink at. Every loop through the main loop, each LED instance is checking if the current software time means they should turn on or off based on how much time has elapsed since they last turned on or off given their respective interval.

## 15. Resources

The code, transcription of the slides, and more links can be found at my Github repo below.

I also recommend checking out Adafruit, and this is a link to their learning site. They have many great diy and easy to learn hardware projects.

## 16. Thank you

Thank you very much. If you have questions, feel free to email me.
