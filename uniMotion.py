import RPi.GPIO as GPIO
import time
import sys

class _:

  def __init__(self, dir_pin, step_pin, en_pin):

    self._dir_pin  = dir_pin
    self._step_pin = step_pin
    self._en_pin   = en_pin

    GPIO.setmode(BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(self._dir_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(self._step_pin, GPIO.OUT, initial=GPIO.LOW)
    
  def oneStep(self, direction):
    
    GPIO.output(self._dir_pin, GPIO.HIGH if direction == CW else GPIO.LOW)
    
    GPIO.output(self._step_pin, GPIO.HIGH)
    time.sleep(.005)
    GPIO.output(self._step_pin, GPIO.LOW)
    time.sleep(.005)
    
  def uniMotion(self):
    
    while True:
      try:
        oneStep(self, self._dir_pin)
      except KeyboardInterrupt:
        break
        
  def Accelerate(self,)
        
