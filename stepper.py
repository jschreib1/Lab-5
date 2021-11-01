from PCF import PCF8591

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  #dir = +/- 1 (ccw /cw)
  stepper.state += dir
  if stepper.state > 7: stepper.state = 0
  elif stepper.state < 0: stepper.state = 7
  for pin in range(4):
    GPIO.output(pins[pin], sequence[stepper.state][pin])

def moveSteps(steps, dir):
  # move the actuation sequence a given number of half steps
  for step in range(steps):
    halfstep(dir)
    #print(step)

class Stepper:
  def __init__(self, address):
    self.PCF8591 = PCF8591(address)
    #PCF8591(0x40)
  
  state = 0 # current position in stator sequence
  current_angle = 0
  
  def getval(self):
    print(self.PCF8591.read(0))
    val = self.PCF8591.read(0)
    return val

  def zero(self, val):
    light = val
    while light < 200:
      moveSteps(512,1)
      light = self.PCF8591.read(0)
    stepper.current_angle = 0
    print(stepper.current_angle)
    return current_angle

def goAngle(self, angle):
  turn_angle = angle - stepper.current_angle
  if abs(turn_angle) < 180:
    moveSteps(angle,1)
  else:
    moveSteps(angle,-1)
      