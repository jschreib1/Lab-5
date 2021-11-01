import RPi.GPIO as GPIO
import time
from stepper import Stepper
from PCF import PCF8591
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)
GPIO.setup(12, GPIO.IN)
# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:

state = 0 # current position in stator sequence
current_angle = 0

sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]



try:
  myADC = PCF8591(0x48)
  myStepper = Stepper(0X48)
  light_level = myStepper.getval()
  myStepper.zero(light_level)
  #myStepper.goAngle(90)

except Exception as e:
  print(e)
  pass
GPIO.cleanup()