from operation import opProfile as OP

import RPi.GPIO as GPIO
import asyncio, time, math

class DRV8825:
    
    def __init__(self,
                 dir_pin_x, step_pin_x, en_pin_x,
                 dir_pin_y, step_pin_y, en_pin_y):
        
        self._dir_pin_x    = dir_pin_x
        self._step_pin_x   = step_pin_x
        self._en_pin_x     = en_pin_x
        
        self._dir_pin_y    = dir_pin_y
        self._step_pin_y   = step_pin_y
        self._en_pin_y     = en_pin_y
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
    def enable(self):
        
        if self._en_pin_x and self._en_pin_y:
            GPIO.setup(self._en_pin_x, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(self._en_pin_y, GPIO.OUT, initial=GPIO.LOW)
        print("EN pins enabled: ", self._en_pin_x, self._en_pin_y)
        
        print("DIR pins are: ", self._dir_pin_x, self._dir_pin_y)
        print("STEP pins are: ", self._step_pin_x, self._step_pin_y)
        
    def disable(self):
        if self._en_pin_x and self._en_pin_y:
            GPIO.setup(self._en_pin_x, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self._en_pin_y, GPIO.OUT, initial=GPIO.HIGH)
        print("EN pins disabled")
        
    def on(self):
        
        GPIO.setup(self._dir_pin_x, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self._step_pin_x, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self._dir_pin_y, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self._step_pin_y, GPIO.OUT, initial=GPIO.LOW)
        

        
    def move_axial(self, motor, direction, stepdelay):
        
            if motor == "X":
                GPIO.output(self._dir_pin_x, GPIO.HIGH if direction==1 else GPIO.LOW)
                GPIO.output(self._step_pin_x, GPIO.LOW)
                time.sleep(stepdelay)
                GPIO.output(self._step_pin_x, GPIO.HIGH)
                time.sleep(stepdelay)
                
            elif motor == "Y":
                GPIO.output(self._dir_pin_y, GPIO.HIGH if direction==1 else GPIO.LOW)
                GPIO.output(self._step_pin_y, GPIO.LOW)
                time.sleep(stepdelay)
                GPIO.output(self._step_pin_y, GPIO.HIGH)
                time.sleep(stepdelay)
            
'''
    async def X(self, _dir_x, _stpdel_x, _tar_stp_x):
        _steps_done_x = 0
        
        while _steps_done_x <= _tar_stp_x:
            print("X current step: ", _steps_done_x)
            GPIO.output(self._dir_pin_x, GPIO.HIGH if _dir_x==1 else GPIO.LOW)
            GPIO.output(self._step_pin_x, GPIO.LOW)
            await asyncio.sleep(_stpdel_x)
            GPIO.output(self._step_pin_x, GPIO.HIGH)
            await asyncio.sleep(_stpdel_x)
            
            _steps_done_x += 1
            
    async def Y(self, _dir_y, _stpdel_y, _tar_stp_y):
        _steps_done_y = 0
        
        while _steps_done_y <= _tar_stp_y:
            print("Y current step: ", _steps_done_y)
            GPIO.output(self._dir_pin_y, GPIO.HIGH if _dir_y==1 else GPIO.LOW)
            GPIO.output(self._step_pin_y, GPIO.LOW)
            await asyncio.sleep(_stpdel_y)
            GPIO.output(self._step_pin_y, GPIO.HIGH)
            await asyncio.sleep(_stpdel_y)
            
            _steps_done_y += 1
            
    async def move_diag(self, displacement_mm, angle_deg, dir_x, dir_y, disptime):

        print("Magnet now moving diagonally")
        
        diag = OP(displacement_mm, angle_deg)
        
        [disp_x, disp_y]   = diag.diag_to_ax()
        
        _ax_x = OP(disp_x)
        _ax_y = OP(disp_y)
        print("x direction STEPs requirement: ", _ax_x.calc_steps())
        print("y direction STEPs requirement: ", _ax_y.calc_steps())
        
        x = asyncio.create_task(self.X(dir_x, disptime/_ax_x.calc_steps(), _ax_x.calc_steps()))
        y = asyncio.create_task(self.Y(dir_y, disptime/_ax_y.calc_steps(), _ax_y.calc_steps()))
        
        await x
        await y
'''
