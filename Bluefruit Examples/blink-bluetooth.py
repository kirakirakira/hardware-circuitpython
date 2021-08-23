# Provide an "eval()" service over BLE UART.

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_circuitplayground import cp
from Timer import BlinkDemo
import time

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

blinkDemo = BlinkDemo(0.5, 5, (255, 0, 0))
blinkDemo2 = BlinkDemo(0.1, 4, (0, 255, 0))

blinkDemo.start()
blinkDemo2.start()

ble.start_advertising(advertisement)
print("Waiting to connect")

while True:
    if cp.button_a:
        cp.play_mp3("punch.mp3")

    blinkDemo.next()
    blinkDemo2.next()

    while not ble.connected:
        pass
    
    s = uart.readline()
    if s:
        try:
            print(s)
            result = str(eval(s))
        except Exception as e:
            result = repr(e)
        print(result)
        uart.write(result.encode("utf-8"))