# Modified from: https://github.com/mikepschneider/CircuitPython_nonblocking_timer

import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground import cp

class NonBlockingTimer(object):
  """ Non blocking timer class for use with CircuitPython """
  _STOPPED = 'STOPPED'
  _RUNNING = 'RUNNING'

  def __init__(self, periodic, interval=-1):
    """Create a new timer with optional interval. Initial state is _STOPPED.
       Call start() to set status to RUNNING. """
    self._interval = interval
    self._status = NonBlockingTimer._STOPPED
    self._periodic = periodic
    self._start_time = 0

  @property
  def status(self):
    """Get Status"""
    return self._status

  def next(self):
    """Returns true or false according to the following algorithm:
      if interval <= 0 raise RuntimeError
      if status != RUNNING return false
      if status == RUNNING and time.monotonic() - start_time > interval
      return True and set start_time = time.monotonic()
      else return False """

    if self._interval <= 0:
      raise RuntimeError('Interval must be > 0')

    if self._status != NonBlockingTimer._RUNNING:
      return False

    current_time = time.monotonic()
    elapsed = current_time - self._start_time

    if elapsed >= self._interval:
    # The timer has been "triggered"
        self._start_time = current_time
        if self._periodic:
            self._status = NonBlockingTimer._STOPPED
        return True
    return False

  def stop(self):
    """Sets status to STOPPED. Do any cleanup here such as releasing pins,
       etc. Call start() to restart. Does not reset start_time."""
    self._status = NonBlockingTimer._STOPPED

  def start(self):
    """Sets status to RUNNING. Sets start_time to time.monotonic(). Call
       next() repeatedly to determine if the timer has been triggered.
       If interval <= 0 raise a RuntimeError """
    if self._interval <= 0:
      raise RuntimeError('Interval must be > 0')

    self._start_time = time.monotonic()
    self._status = NonBlockingTimer._RUNNING

  def set_interval(self, seconds):
    """ Set the trigger interval time in seconds (float). If interval <= 0
        raise a RuntimeError """
    if seconds <= 0:
      raise RuntimeError('Interval must be > 0')
    self._interval = seconds

  def get_interval(self):
    """Get interval"""
    return self._interval


class BlinkDemo(NonBlockingTimer):
    def __init__(self, interval, index, color):
        super(BlinkDemo, self).__init__(False, interval)
        self.index = index
        self.color = color
        cp.pixels[self.index] = self.color
        cp.pixels.brightness = 0.05
    def stop(self):
        cp.pixels[self.index] = (0, 0, 0)
        super(BlinkDemo, self).stop()
    def next(self):
        if (super(BlinkDemo, self).next()):
            if cp.pixels[self.index] == (0, 0, 0):
                cp.pixels[self.index] = self.color
            else:
                cp.pixels[self.index] = (0, 0, 0)

class LongDemo(NonBlockingTimer):
    def __init__(self, interval):
        super(LongDemo, self).__init__(True, interval)
    def stop(self):
        return (super(LongDemo, self).stop())
    def next(self):
        return (super(LongDemo, self).next())

blinkDemo = BlinkDemo(0.5, 5, (255, 0, 0))
blinkDemo2 = BlinkDemo(0.1, 4, (0, 255, 0))
blinkDemo3 = BlinkDemo(0.75, 3, (0, 0, 255))
blinkDemo4 = BlinkDemo(0.6, 2, (125, 125, 125))

blinkDemo.start()
blinkDemo2.start()

longDemo = LongDemo(10)
longDemo.start()

while True:
    blinkDemo.next()
    blinkDemo2.next()
    blinkDemo3.next()
    blinkDemo4.next()

    if longDemo.next():
        print("you're the bomb dot com")
        blinkDemo3.start()
    
    if cp.switch:
        blinkDemo4.start()

    # This is the only place you should use time.sleep: to set the overall
    # "sampling rate" of your program.
    time.sleep(0.001)