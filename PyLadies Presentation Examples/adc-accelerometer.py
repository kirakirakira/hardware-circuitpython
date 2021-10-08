from adafruit_circuitplayground import cp
import time

pink = (200, 0, 200)
clear = (0, 0, 0)
cp.pixels.brightness = 0.1
delay_time = 0.05

while True:
    for pixel in range(10):
        cp.pixels[pixel] = pink
        time.sleep(delay_time)

        cp.pixels[pixel] = clear
        delay_time = abs(cp.acceleration.z - 10)* 0.03