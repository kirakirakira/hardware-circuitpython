# Modified from https://learn.adafruit.com/PyRulerVideoPanic/code
# Keyboard shortcuts work in Microsoft Teams

import os
import board
from digitalio import DigitalInOut, Direction
import time
import touchio
import adafruit_dotstar

leddot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
leddot[0] = (128, 0, 128)
leddot.brightness = 0.3

# Set this to True to turn the touchpads into a keyboard
ENABLE_KEYBOARD = True

# Used if we do HID output, see below
if ENABLE_KEYBOARD:
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keycode import Keycode
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
    kbd = Keyboard()
    layout = KeyboardLayoutUS(kbd)

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

touches = [DigitalInOut(board.CAP0)]
for p in (board.CAP1, board.CAP2, board.CAP3):
    touches.append(touchio.TouchIn(p))

leds = []
for p in (board.LED4, board.LED5, board.LED6, board.LED7):
    led = DigitalInOut(p)
    led.direction = Direction.OUTPUT
    led.value = True
    time.sleep(0.25)
    leds.append(led)
for led in leds:
    led.value = False


cap_touches = [False, False, False, False]


def read_caps():
    t0_count = 0
    t0 = touches[0]
    t0.direction = Direction.OUTPUT
    t0.value = True
    t0.direction = Direction.INPUT
    # funky idea but we can 'diy' the one non-hardware captouch device by hand
    # by reading the drooping voltage on a tri-state pin.
    t0_count = t0.value + t0.value + t0.value + t0.value + t0.value + \
        t0.value + t0.value + t0.value + t0.value + t0.value + \
        t0.value + t0.value + t0.value + t0.value + t0.value
    cap_touches[0] = t0_count > 2
    cap_touches[1] = touches[1].raw_value > 3000
    cap_touches[2] = touches[2].raw_value > 3000
    cap_touches[3] = touches[3].raw_value > 3000
    return cap_touches


def type_alt_code(code):
    kbd.press(Keycode.CONTROL, Keycode.SHIFT)
    kbd.press(Keycode.U)
    kbd.release_all()
    kbd.send(Keycode.TWO)
    kbd.send(Keycode.ONE)
    kbd.send(Keycode.TWO)
    kbd.send(Keycode.SIX)
    kbd.send(Keycode.ENTER)


def show_command_palette():
    kbd.press(Keycode.CONTROL, Keycode.SHIFT)
    kbd.press(Keycode.P)
    kbd.release_all()


def search():
    kbd.press(Keycode.CONTROL)
    kbd.press(Keycode.F)
    kbd.release_all()


def go_to_file():
    kbd.press(Keycode.CONTROL)
    kbd.press(Keycode.P)
    kbd.release_all()


while True:
    caps = read_caps()
    # light up the matching LED
    for i, c in enumerate(caps):
        leds[i].value = c
    if caps[0]:
        if ENABLE_KEYBOARD:
            go_to_file()
    if caps[1]:
        if ENABLE_KEYBOARD:
            show_command_palette()
    if caps[2]:
        if ENABLE_KEYBOARD:
            search()
    if caps[3]:
        if ENABLE_KEYBOARD:
            layout.write('LGTM :+1:')
    time.sleep(0.1)

