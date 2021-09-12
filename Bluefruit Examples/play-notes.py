from adafruit_circuitplayground import cp
import time
import random

scale = [523, 587, 659, 698, 784, 880, 988, 1047]
melody = [0, 0, 4, 4, 5, 5, 4]
num_repeats = 5

# for i in range(num_repeats):
#     for note in melody:
#         cp.play_tone(scale[note], 0.25)
#     time.sleep(1)

for i in range(20):
    cp.play_tone(random.choice(scale), 0.25)