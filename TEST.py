from operation import opProfile as OP
from run import DRV8825 as DRV
import asyncio, time, math

X_DIR = 20
X_STEP = 16
X_EN = 21

Y_DIR = 19
Y_STEP = 13
Y_EN = 26

R = DRV(X_DIR, X_STEP, X_EN, Y_DIR, Y_STEP, Y_EN)

R.enable()

R.on()

time.sleep(2)

R.move_axial('X', 50, 1, .005)

time.sleep(2)

R.move_axial('Y', 30 ,0, .005)

asyncio.run(R.move_diag(50,30,1,1,5))
