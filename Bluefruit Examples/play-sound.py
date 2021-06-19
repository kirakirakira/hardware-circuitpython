from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.1

while True:
    if cp.button_a:
        cp.play_mp3("radio-tune.mp3")
    if cp.button_b:
        cp.play_mp3("punch.mp3")
    if cp.loud_sound(sound_threshold = 250):
        cp.pixels.fill((50, 0, 50))
        time.sleep(0.2)
    else:
        cp.pixels.fill((0, 0, 0))