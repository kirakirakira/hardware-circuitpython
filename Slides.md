# Script to go with slides

## 1. Title

Welcome to Basics of Hardware with a PyRuler! My name is Kira Hartlage, and I will be teaching you a bit about hardware and how you can get started using Python.

## 2. Desired Outcomes

Here are our desired outcomes for our time together. I’ll introduce to you a bit about embedded firmware development. I’ll introduce how you can use CircuitPython as an alternative to C. We’ll look at an example of how to write code for hardware using the PyRuler. Then I’ll show you resources and examples of projects that you can explore to learn on your own.

## 3. Introduction

As I said, my name is Kira Hartlage. I have a background in mechanical engineering and consumer appliance part design. I started my software journey teaching myself Python using EdX and other online courses before branching out and switching to embedded development at my current company, still working on consumer appliances. Today, I act as a scrum master and software developer for an exciting new home appliance that will allow you to have a garden in your home year-round.

## 4. Agenda

## 5. Embedded systems

We will start with what is embedded firmware or is it embedded software or maybe embedded systems?

A book I recommend if you’re interested in learning more about embedded systems is Making Embedded Systems by Elecia White. She also has a podcast called EmbeddedFM.

https://www.amazon.com/Making-Embedded-Systems-Patterns-Software/dp/1449302149

Embedded software development is basically writing code to control a device that is not a computer. So you typically don’t have an operating system,and you will be dealing with memory and time constraints for the particular device that you’re writing code for. Embedded software can also be called firmware as firmware is stored in non-volatile memory such as ROM, Flash, or EEPROM. In the past, you would not be able to update the device’s codeset, hence it was firm. But nowadays there are methods to update non-volatile memory without too much headache.

## 6. Hardware - Microcontrollers

https://embedded.fm/blog/2016/2/27/embedded-software-engineering-101-microcontroller-basics

## 7. Hardware - Peripherals

https://embedded.fm/blog/2016/5/16/ese101-peripherals-part-1
https://embeddedinventor.com/9-essential-microcontroller-peripherals-explained/

## 8. CircuitPython

https://github.com/adafruit/circuitpython
https://circuitpython.org/
Example guides: https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/CircuitPython_Essentials

CircuitPython is a derivative of MicroPython and it was developed by Adafruit as an easy way to program microcontrollers with education as the primary objective.

There are many low-cost microcontroller boards, and with CircuitPython there are no special desktop software requirements. You can use any text editor to start editing code. You won’t need to install a fancy compiler or need any special equipment to upload code either. Since CircuitPython is based on Python, it’s also easy to transition and get started with little prior programming experience.

CircuitPython code lives on the board itself, so you are able to take it with you and edit it on whatever and whenever you like. There is also a serial console and REPL that you can set up to allow for live feedback and for interactive programming. There are many libraries and drivers for various sensor, components, and boards so you don’t have to write your own from scratch.

## 9. PyRuler

The PyRuler is a ruler...and it’s a reference board that shows you what various PCB (printed circuit board) components look like, their name and their size. But it also has a few cool features that makes it a simple board to get started with in your CircuitPython journey.

It has a Trinket M0 (a Cortex M0 microcontroller), as well as 4 capacitive touch pads with matching LEDs. It comes with code already loaded it on, so all you need to do is plug and play. Each of 3 of the capacitive touch buttons will press a Greek symbol as keyboard input on your computer. You’ll no longer need to remember the keyboard shortcut for omega, mu, or pi ever again! If you press the Digi-Key logo, it prints the URL for Digi-Key’s Python on hardware guide.

Because the code is already there, it makes it easy to edit and change what is printed.

<some other projects: 1. printing other words, 2. Conference call muting>

## 10. Capactive Touch Buttons

https://en.wikipedia.org/wiki/Capacitive_sensing
https://learn.adafruit.com/adafruit-pyruler/circuitpython-cap-touch

## 11. PyRuler Project  #1
Hello, World blinking when pressing cap touch buttons and printing to screen

## 12. PyRuler Project #2
Muting conference call and turning on/off camera

## 13. Circuit Playground Express/Bluefruit
https://learn.adafruit.com/adafruit-circuit-playground-express
https://www.adafruit.com/product/4333

## 14. Circuit Playground Express/Bluefruit Project
Scheduling blinking lights

## 15. Resources

## 16. Thank you