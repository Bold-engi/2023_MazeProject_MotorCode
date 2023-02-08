import RPi.GPIO as GPIO
import time

class DRV8825:
  
  def __init__(self, dir_pin, step_pin, en_pin):
    
    self._dir_pin = dir_pin
    self._step_pin = step_pin
    self._en_pin = en_pin
    
  def enable(self):
    if self._en_pin:
      GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.LOW)
    print('Driver enabled')
      
  def disable(self):
    if self._en_pin:
      GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.HIGH)
    print('Driver disabled')
      
  def on(self):
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(self._dir_pin, GPIO.OUT, inital=GPIO.HIGH)
    GPIO.setup(self._step_pin, GPIO.OUT, inital=GPIO.LOW)
    
    enable()
    
  def off(self):
    disable()
    
  def oneStep(self, direction):
    
    GPIO.output(self._dir_pin, GPIO.HIGH if direction==1 else GPIO.LOW)
    
    GPIO.output(self._step_pin, GPIO.HIGH)
    time.sleep(.005)
    GPIO.output(self._step_pin, GPIO.LOW)
