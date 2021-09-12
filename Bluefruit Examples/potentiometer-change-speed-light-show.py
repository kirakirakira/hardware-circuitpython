import time
from adafruit_circuitplayground import cp
import board
import analogio

cp.pixels.brightness = 0.05
cp.pixels.auto_write = False

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clear = (0, 0, 0)

colors = [red, green, blue]

pixel = 0
color_index = 0

knob = analogio.AnalogIn(board.A6)

while True:
    for color in colors:
        delay_time = round(knob.value/65535 * 100)
        print(delay_time/1000)
        cp.pixels[pixel] = color
        pixel = (pixel + 1) % 10
        cp.pixels.show()
        time.sleep(delay_time/1000)