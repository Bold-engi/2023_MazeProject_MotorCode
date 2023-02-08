import numpy

class DispProfile:
  
  def __init__(self):
    # self-explained
    self._rotor_radius_mm = 4.5/2
    
  def set_distance(self, distance_mm):
    self._distance_mm = distance_mm
  
  def calc_steps(self):
    # calculate steps required to achieve the target displacement
    return round((self._distance_mm/self._rotor_radius_mm)*(180/numpy.pi))
