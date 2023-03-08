import math

class opProfile:
    
    def __init__(self, distance_mm, angle=None):
        
        self._distance      = distance_mm * 10
        self._distance_mm   = distance_mm
        self._angle_deg     = angle
        
        self._rt_radius_mm  = 4.5/2
        self._step_angle    = 1.8
        
        self._distp_x       = 0
        self._distp_y       = 0

    def calc_steps(self):
        '''
        Returns steps requiered to move a certain displacement
        '''
        return round(self._distance/(self._rt_radius_mm * self._step_angle))
    
    def diag_to_ax(self):
        '''
        Returns axial displacement
        
        POSITIVE regardless x-axis is +ve or -ve
        Less than 90 degrees
        '''
        return [self._distance_mm * math.cos(math.radians(self._angle_deg)),
                self._distance_mm * math.sin(math.radians(self._angle_deg))]
    
'''
    def disp_per_step(self):     
        [self._distp_x, self._distp_y] = self.diag_to_ax()
        return [round(self._distp_x/self.calc_steps(), 2),
                round(self._distp_y/self.calc_steps(), 2)]
'''