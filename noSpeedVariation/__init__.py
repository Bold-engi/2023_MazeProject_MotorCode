import numpy

class opProfile:
  
  def __init__(self):
    
    # Self-explained
    self._direction       = CW
    self._cur_steps       = 0
    self._target_steps    = 0
    self._rotor_radius_mm = 4.5/2
    
  def set_distance(self, distance_mm):
    self._distance_mm = distance_mm
  
  def calc_steps(self):
    # calculate steps required to achieve the target displacement
    return round((self._distance_mm/self._rotor_radius_mm)*(180/numpy.pi))

  def set_target_steps(self):
    self._target_steps = self.calc_steps()
    
  def current_steps(self):
    
    if self._direction == CW:
      self._cur_steps += 1
    elif self._direction == CCW:
      self._cur_steps -= 1
