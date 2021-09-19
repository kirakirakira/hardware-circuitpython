# Do this in terminal:
# cat /dev/ttyACM0 | tee -a acceleration.csv

from adafruit_circuitplayground import cp
import time

steps = 0

while True:
    print("steps = {}".format(steps), end = "\n")
    # print("steps = " + str(steps), end = "\n")
    print("{}, {}, {}".format(cp.acceleration.x, cp.acceleration.y, cp.acceleration.z), end="\r")

    if cp.acceleration.x < 2 and cp.acceleration.y > 10:
        steps+=1


    time.sleep(0.5)