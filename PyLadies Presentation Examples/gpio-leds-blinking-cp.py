from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led = True
    time.sleep(1)
    cp.red_led = False
    time.sleep(1)