from adafruit_circuitplayground import cp
import time
import board
import analogio

cp.pixels.brightness = 0.05
cp.pixels.auto_write = False

knob = analogio.AnalogIn(board.A6)

while True:
    cp.pixels.fill((255, 0, 0))
    pot_value = round(knob.value/65535 * 100)
    cp.pixels.brightness = pot_value/100
    cp.pixels.show()
    time.sleep(0.1)