import time
from adafruit_circuitplayground import cp

scale = [523, 587, 659, 698, 784, 880, 988]

cp.adjust_touch_threshold(200)

while True:
    if cp.touch_A1:
        cp.play_tone(scale[0], 0.25)
    if cp.touch_A2:
        cp.play_tone(scale[1], 0.25)
    if cp.touch_A3:
        cp.play_tone(scale[2], 0.25)
    if cp.touch_A4:
        cp.play_tone(scale[3], 0.25)
    if cp.touch_A5:
        cp.play_tone(scale[4], 0.25)
    if cp.touch_A6:
        cp.play_tone(scale[5], 0.25)
    if cp.touch_TX:
        cp.play_tone(scale[6], 0.25)

    time.sleep(0.05)
