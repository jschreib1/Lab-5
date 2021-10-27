from PCF import PCF8591

class Stepper:
  def __init__(self, address):
    self.PCF8591 = PCF8591(address)
    #PCF8591(0x40)
  def getval(self):
    #print(PCF8591.read(0))
    val = self.PCF8591.read(0)
    return val

  def zero(val):
    while val > 125:
      moveSteps(512,1)
    current_angle = 0
    return current_angle

def goAngle(angle):
  turn_angle = angle - current_angle
  if abs(turn_angle) < 180:
    moveSteps(angle,1)
  else:
    moveSteps(angle,-1)
      