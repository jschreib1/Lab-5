import RPi.GPIO as GPIO
import time
from PCF import PCF8591
GPIO.setwarnings(False)




class Stepper:
  def __init__(self, address):
    self.PCF8591 = PCF8591(address)
    #PCF8591(0x40)
    self.state = 0 # current position in stator sequence
    self.current_angle = 0
    GPIO.setmode(GPIO.BCM)
    self.pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
    for pin in self.pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)
    GPIO.setup(12, GPIO.IN)
    self.led_pin = 16
    GPIO.setup(self.led_pin, GPIO.OUT)
    # Define the pin sequence for counter-clockwise motion, noting that
    # two adjacent phases must be actuated together before stepping to
    # a new phase so that the rotor is pulled in the right direction:



    sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
    [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
  
  def getval(self):
    print(self.PCF8591.read(0))
    val = self.PCF8591.read(0)
    return val

  def halfstep(self, dir):
    #dir = +/- 1 (ccw /cw)
    Stepper.state += dir
    if Stepper.state > 7: Stepper.state = 0
    elif Stepper.state < 0: Stepper.state = 7
    for pin in range(4):
      GPIO.output(self.pins[pin], sequence[Stepper.state][pin])

  def moveSteps(self, steps, dir):
    # move the actuation sequence a given number of half steps
    for step in range(steps):
      halfstep(dir)
      #print(step)      

  def zero(self, val):
    light = val
    GPIO.output(self.led_pin, 1)
    '''
    while light < 200:
      moveSteps(10,1)
      light = self.PCF8591.read(0)
      '''
    print(self.PCF8591.read(0))
    GPIO.output(self.led_pin, 0)
    Stepper.current_angle = 0
    print(Stepper.current_angle)
    return current_angle

  def goAngle(self, angle):
    turn_angle = angle - Stepper.current_angle
    if abs(turn_angle) < 180:
      moveSteps(angle,1)
    else:
      moveSteps(angle,-1)

  def delay_us(self, tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass

  