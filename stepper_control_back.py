import RPi.GPIO as GPIO
import time
from stepper import Stepper
from PCF import PCF8591
GPIO.setmode(GPIO.BCM)
pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)
GPIO.setup(12, GPIO.IN, initial=0)
# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:

sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0 # current position in stator sequence
current_angle = 0


def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  #dir = +/- 1 (ccw /cw)
  state += dir
  if state > 7: state = 0
  elif state < 0: state = 7
  for pin in range(4):
    GPIO.output(pins[pin], sequence[state][pin])

def moveSteps(steps, dir):
  # move the actuation sequence a given number of half steps
  for step in steps:
    halfstep(dir)



try:
  myADC = PCF8591(0x48)
  light_level = myADC.getval()
  myStepper = Stepper(0X48)
  myStepper.zero(light_level)
  myStepper.goAngle(90)

except Exception as e:
  print(e)
  pass
GPIO.cleanup()