import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
red = (255, 0, 0)
clear = (0, 0, 0)
green = (79, 240, 98)
blue = (66, 48, 219)
teal = (0, 126, 80)
pink = (250, 50, 174)

colors = [teal, pink, green, blue]

color_index = 0

while True:
    pixel = 0

    while pixel < 10:
        cp.pixels[pixel] = colors[color_index]
        time.sleep(0.2)
        pixel += 1

    pixel = 9

    while pixel >= 0:
        cp.pixels[pixel] = clear
        time.sleep(0.2)
        pixel -= 1

    if color_index == len(colors) - 1:
        color_index = 0
    else:
        color_index += 1