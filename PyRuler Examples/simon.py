# Modified from https://learn.adafruit.com/simon-game-with-pyruler-and-circuitpython/code-pyruler-with-circuitpython

import os
import board
from digitalio import DigitalInOut, Direction
import time
import touchio
import adafruit_dotstar
import random

leddot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
leddot[0] = (128, 0, 128)
leddot.brightness = 0.3

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

touches = [DigitalInOut(board.CAP0)]
for p in (board.CAP1, board.CAP2, board.CAP3):
    touches.append(touchio.TouchIn(p))

leds = []
for p in (board.LED4, board.LED5, board.LED6, board.LED7):
    led = DigitalInOut(p)
    led.direction = Direction.OUTPUT
    leds.append(led)

def light_cap_led(cap, duration = 0.5):
    leds[cap].value = True
    time.sleep(duration)
    leds[cap].value = False
    time.sleep(duration)

def light_up_sequence(sequence):
    for cap in sequence:
        light_cap_led(cap, 0.35)

light_up_sequence([0, 1, 2, 3, 2, 1, 0])

cap_touches = [False, False, False, False]
time_now = time.monotonic()
caps_touched = []

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

time_now = time.monotonic()

def time_passed():
    time_pressed = time.monotonic()
    time_passed = time_pressed - time_now
    return time_passed

def timeout_touch(timeout = 3):
	start_time = time.monotonic()
	while time.monotonic() - start_time < timeout:
		caps = read_caps() # return cap_touches which will have True if that cap is touched
		# i is cap number, c is True or False (whether or not it was touched)
		for i, c in enumerate(caps):
			if c:
				return i # cap number

def read_sequence(sequence):
	for cap in sequence:
		# 3 second timer starts for each cap in the sequence
		if timeout_touch() != cap:
			return False
		light_cap_led(cap, 0.5)
	return True

sequence = []

while True:
	time.sleep(1)
	sequence.append(random.randint(0, 3))
	print(sequence)
	light_up_sequence(sequence)

	if not read_sequence(sequence):
		time.sleep(3)
		print("game over")
		break
	else:
		print("next sequence unlocked!")
	time.sleep(1)