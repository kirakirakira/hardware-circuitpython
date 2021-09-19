# Do this in terminal:
# cat /dev/ttyACM0 | tee -a acceleration.csv

from adafruit_circuitplayground import cp
import time

while True:
    print("{}, {}, {}".format(cp.acceleration.x, cp.acceleration.y, cp.acceleration.z), end="\r")
    time.sleep(0.5)