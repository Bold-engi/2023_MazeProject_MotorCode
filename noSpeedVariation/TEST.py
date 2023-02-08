from operation import opProfile
from setup import DRV8825
import RPi.GPIO as GPIO
import numpy, time

DIR = 16
STEP = 12
EN = 18

op = opProfile()
drv = DRV8825(DIR, STEP, EN)

drv.on()
op.set_distance(100)
t_steps = op.set_target_steps()
c_step  = op.current_step()

while c_step <= t_steps:
  drv.oneStep(1)
  time.sleep(.005)
