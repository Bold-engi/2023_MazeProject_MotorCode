import numpy

class opProfile:
    
    def __init__(self):
        
        self._cur_step      = -1
        self._steps_done    = 0
        self._tar_steps     = 0
        self._rt_radius_mm  = 4.5/2
        
    def set_distance(self, distance_mm):
        self._distance_mm = distance_mm
        print("DISTANCE(mm) = ", self._distance_mm)
        
    def calc_steps(self):
        return round((self._distance_mm/self._rt_radius_mm)*(180/numpy.pi))
    
    def set_target_steps(self):
        self._tar_steps = self.calc_steps()
        return self._tar_steps
        
    def current_step(self):
        self._cur_step += 1
        return self._cur_step
