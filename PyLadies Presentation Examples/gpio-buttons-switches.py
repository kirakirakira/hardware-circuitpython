from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.01

green = (0, 255, 0)
pink = (255, 100, 150)
red = (255, 0, 0)
yellow = (255, 255, 0)

while True:
    if cp.switch:
        cp.pixels.fill(green)
    else:
        if cp.button_a:
            cp.pixels.fill(pink)
        elif cp.button_b:
            cp.pixels.fill(yellow)
        else:
            cp.pixels.fill(red)