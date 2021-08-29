import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

def blink_led(sleep_time):
    led.value = True
    time.sleep(sleep_time)
    led.value = False
    time.sleep(sleep_time)

def speed_up(sleep_time):
    while sleep_time > 0.2:
        print("I'm speeding up")
        blink_led(sleep_time)
        sleep_time = sleep_time * 0.8
        print(sleep_time)

def slow_down(sleep_time):
    while sleep_time < 2:
        print("I'm slowing down")
        blink_led(sleep_time)
        sleep_time = sleep_time / 0.8
        print(sleep_time)

while True:
    sleep_time = 0.5
    speed_up(sleep_time)
    sleep_time = 0.5
    slow_down(sleep_time)
