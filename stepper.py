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



    self.sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
    [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
  
  def getval(self):
    print(self.PCF8591.read(0))
    val = self.PCF8591.read(0)
    return val

  def halfstep(self, dir):
    #dir = +/- 1 (ccw /cw)
    self.state += dir
    if self.state > 7: self.state = 0
    elif self.state < 0: self.state = 7
    for pin in range(4):
      GPIO.output(self.pins[pin], self.sequence[self.state][pin])

  def moveSteps(self, steps, dir):
    # move the actuation sequence a given number of half steps
    for step in range(steps):
      self.halfstep(dir)
      #print(step)      

  def zero(self):
    light = self.PCF8591.read(0)
    GPIO.output(self.led_pin, 1)
    while light < 200:
      self.moveSteps(500,1)
      light = self.PCF8591.read(0)
    print(self.PCF8591.read(0))
    GPIO.output(self.led_pin, 0)
    self.current_angle = 0
    print(self.current_angle)
    return self.current_angle

  def goAngle(self, angle):
    turn_angle = angle - self.current_angle
    if abs(turn_angle) < 180:
      self.moveSteps(angle,1)
    else:
      self.moveSteps(angle,-1)

  def delay_us(self, tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass

  