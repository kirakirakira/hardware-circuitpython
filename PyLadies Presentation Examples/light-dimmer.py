from adafruit_circuitplayground import cp
import time
import board
import analogio

cp.pixels.brightness = 0.05
cp.pixels.auto_write = False

pink = (250, 50, 174)
blue = (0, 0, 255)
green = (0, 255, 0)

knob_x = analogio.AnalogIn(board.A6)
knob_y = analogio.AnalogIn(board.A5)

while True:
    pot_value_x = round(knob_x.value/65535 * 100)
    pot_value_y = round(knob_y.value/65535 * 100)
    print(pot_value_x, pot_value_y)
    brightness = (pot_value_x + pot_value_y)/2000
    print("brightness ", brightness)
    cp.pixels.brightness = brightness
    if brightness < 0.03:
        cp.pixels.fill(blue)
    elif brightness < 0.05:
        cp.pixels.fill(green)
    else:
        cp.pixels.fill(pink)
    cp.pixels.show()
    time.sleep(0.1)
