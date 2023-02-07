class pwmProfile:
  
  def __init__(self, pulse_width=0.000):
    self.pulse_width = pulse_width
    
  def to_rpm(self):
    return (0.300*(0.500/self.pulse_width))
  
  @property
  def pulse_width(self):
    print("Getting pulse width...")
    return self._pulse_width
  
  @pulse_width.setter
  def pulse_width(self, value):
    print("Converting to RPM...")
    
    if value <= 0.000:
      raise ValueError("pulse width cannot be less or equal than 0")
    self._pulse_width = value
