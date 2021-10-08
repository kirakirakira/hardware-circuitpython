# Provide an "eval()" service over BLE UART.

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_circuitplayground import cp
import time

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)
print("Waiting to connect")

while True:
    while not ble.connected:
        pass

    result = (cp.acceleration.x, cp.acceleration.y, cp.acceleration.z)

    if result:
        try:
            uart.write(str(result).encode("utf-8"))
        except Exception as e:
            print(repr(e))

    time.sleep(0.5)