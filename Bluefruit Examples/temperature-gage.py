from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.01

delay_time = 0.5

colors = [(0, 0, 200), (0, 0, 220), (0, 0, 255),
            (100, 0, 215), (200, 0, 150), (200, 0, 200),
            (215, 0, 40), (255, 0, 0), (255, 0, 0), (255, 0, 0)]

while True:
    print(cp.temperature)
    print(cp.temperature * 9/5 + 32)
    temperature = cp.temperature
    # temperature = 20
    for pixel in range(min(temperature / 4, 10)):
        cp.pixels[pixel] = colors[pixel]
    time.sleep(delay_time)