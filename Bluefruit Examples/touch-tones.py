# Alternative to using touchio
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        cp.start_tone(523)
    elif cp.touch_A2:
        cp.start_tone(587)
    else:
        cp.stop_tone()