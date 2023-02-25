from operation import opProfile
from setup import DRV8825
import RPi.GPIO as GPIO
import numpy, time

DIR = 20
STEP = 21
EN = 16

op = opProfile()
drv = DRV8825(DIR, STEP, EN)

drv.enable()
drv.on()
op.set_distance(5)
t_steps = op.set_target_steps()
c_step  = op.current_step()

while c_step <= t_steps:
    drv.oneStep(0)
    time.sleep(.01)
