from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.05

temperature_reference = cp.temperature

while True:
    print(cp.temperature)
    if cp.temperature - temperature_reference > 0.1:
        cp.pixels.fill((255, 0, 0))
    else:
        cp.pixels.fill(0)

    time.sleep(0.25)