import RPi.GPIO as GPIO
from PCF import PCF8591
from stepper import Stepper
import time



try:
  myADC = PCF8591(0x48)
  myStepper = Stepper(0x48)
  light_level = myStepper.getval()
  while True:
    myStepper.halfstep(1)
    print('hello')
  myStepper.zero()
  #myStepper.goAngle(90)

except Exception as e:
  print(e)
  pass
GPIO.cleanup()