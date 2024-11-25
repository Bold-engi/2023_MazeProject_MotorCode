"""
2024 Nov update

This is the file where the drivier IC would drive the motor based on the command sent from
image processing system.
"""
from operation import opProfile as OP
from run import DRV8825 as DRV
import time, math, client, socket

X_DIR = 20
X_STEP = 16
X_EN = 21

Y_DIR = 19
Y_STEP = 13
Y_EN = 26

client.connect()
data = client.receive()

direction = 1
axis = 'X'

R = DRV(X_DIR, X_STEP, X_EN, Y_DIR, Y_STEP, Y_EN)

R.enable()

R.on()

while True:
  '''
  code to run the motor based on received data
  '''
