import board
import neopixel
import touchio

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.chase import Chase

touch_1 = touchio.TouchIn(board.A1)
touch_2 = touchio.TouchIn(board.A2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.05, auto_write = False)

animation_blink = Blink(pixels, color = (0, 255, 0), speed = 0.4)
animation_chase = Chase(pixels, speed = 0.03, color = (255, 0, 0), size = 2, reverse = False)

animation = None
pixels.fill(0)
pixels.show()

while True:
    if animation is not None:
        animation.animate()
    
    if touch_1.value:
        animation = animation_blink

    elif touch_2.value:
        animation = animation_chase