from adafruit_circuitplayground import cp
import time

while True:
    print("light on")
    time.sleep(1)
    print("light off")
    cp.red_led = False
    time.sleep(1)