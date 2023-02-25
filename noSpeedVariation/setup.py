import RPi.GPIO as GPIO
import time

class DRV8825:
    
    def __init__(self, dir_pin, step_pin, en_pin):
        
        self._dir_pin  = dir_pin
        self._step_pin = step_pin
        self._en_pin   = en_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
    def enable(self):
        if self._en_pin:
            GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.LOW)
        print("DRIVER ENABLED")
        
    def disable(self):
        if self._en_pin:
            GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.HIGH)
        print("DRIVER DISABLED")
        
    def on(self):
        
        GPIO.setup(self._dir_pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self._step_pin, GPIO.OUT, initial=GPIO.LOW)
        
    def oneStep(self, direction, stepdelay):
        
        GPIO.output(self._dir_pin, GPIO.HIGH if direction==1 else GPIO.LOW)
        print("DIR pin is: ", self._dir_pin)
        
        GPIO.output(self._step_pin, GPIO.LOW)
        print("STEP: ", self._step_pin)
        time.sleep(stepdelay)
        GPIO.output(self._step_pin, GPIO.HIGH)
        print("STEP: ", self._step_pin)
