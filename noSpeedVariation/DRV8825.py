import RPi.GPIO as GPIO
import time

class DRV8825:
  
  def __init__(self, DIR, STEP, EN):
    
    self._DIR = DIR
    self._STEP = STEP
    self._EN = EN
    
  def enable(self):
    if self._EN:
      GPIO.setup(self._EN, GPIO.OUT, initial=GPIO.LOW)
      
  def disable(self):
    if self._EN:
      GPIO.setup(self._EN, GPIO.OUT, initial=GPIO.HIGH)
      
  def activate(self):
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(self._DIR, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(self._STEP, GPIO.OUT, initial=GPIO.LOW)
    
    self.enable()
    
  def shutdown(self):
    self.disable()
    
  def oneStep(self, dir):
    
    GPIO.output(self._DIR, GPIO.HIGH if dir==1 else GPIO.LOW)
    
    GPIO.output(self._STEP, GPIO.LOW)
    time.sleep(.005)
    GPIO.output(self._STEP, GPIO.HIGH)
    time.sleep(.005)
