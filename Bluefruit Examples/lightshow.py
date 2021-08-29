import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clear = (0, 0, 0)

colors = [red, green, blue]

pixel = 0
color_index = 0

while True:
    for color in colors:
        cp.pixels[pixel] = color
        pixel = (pixel + 1) % 10
        time.sleep(0.01)