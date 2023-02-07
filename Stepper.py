import RPi.GPIO as GPIO
import time
import sys

class Stepper:

  def __init__(self, dir_pin, step_pin, en_pin):

    self._dir_pin  = dir_pin
    self._step_pin = step_pin
    self._en_pin   = en_pin

    GPIO.setmode(BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(self._dir_pin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(self._step_pin, GPIO.OUT, initial=GPIO.LOW)
    
  def enable(self):
    if self._en_pin:
      GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.LOW)
      
  def disable(self):
    if self._en_pin:
      GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.HIGH)
    
  def oneStep(self, step_dir):
    
    GPIO.output(self._dir_pin, GPIO.HIGH if step_dir == 'CW' else GPIO.LOW)
    
    GPIO.output(self._step_pin, GPIO.HIGH)
    time.sleep(.005)
    GPIO.output(self._step_pin, GPIO.LOW)
    time.sleep(.005)
    
  def uniMotion(self):
    
    while True:
      try:
        oneStep(self._dir_pin)
      except KeyboardInterrupt:
        print("User keyboard interrupt detected, program ceases")
        break
        
  def Accelerate(self, accel, accel_dir):
    
    
        
