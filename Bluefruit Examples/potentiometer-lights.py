from adafruit_circuitplayground import cp
import time
import board
import analogio

cp.pixels.brightness = 0.05
cp.pixels.auto_write = False

knob = analogio.AnalogIn(board.A6)

while True:
    cp.pixels.fill(0)
    number_of_pixels = round(knob.value/65535 * 10)
    for p in range(number_of_pixels):
        if number_of_pixels < 4:
            cp.pixels[p] = (255, 0, 0)
        elif number_of_pixels < 7:
            cp.pixels[p] = (0, 255, 0)
        else:
            cp.pixels[p] = (0, 0, 255)
    cp.pixels.show()
    time.sleep(0.1)