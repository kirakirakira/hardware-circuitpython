import time
import usb_hid
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

while True:
    if cp.button_a:
        kbd.release(Keycode.A)
        kbd.press(Keycode.D)
    elif cp.button_b:
        kbd.release(Keycode.D)
        kbd.press(Keycode.A)
    else:
        kbd.release_all() 
    time.sleep(0.01)
