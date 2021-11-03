import RPi.GPIO as GPIO
from PCF import PCF8591
from stepper import Stepper
import time



try:
  myStepper = Stepper(0x48)
  #myStepper.zero()
  myStepper.goAngle(90)

except Exception as e:
  print(e)
  pass
GPIO.cleanup()