from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.1

delay_time = 0.05

while True:
    for pixel in range(10):
        cp.pixels[pixel] = (0, 0, 255)
        time.sleep(delay_time)
        cp.pixels[pixel] = (0)
        # print(cp.acceleration.z)
        delay_time = abs(cp.acceleration.z - 10)* 0.05
        print(delay_time)