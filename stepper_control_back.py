import RPi.GPIO as GPIO
from PCF import PCF8591
from stepper import Stepper
import time
import json



try:
  while True:
    myStepper = Stepper(0x48)
    with open("angle.txt", 'r'):
      json.load(f)
      angle = int(data['Angle'])
      pressed = data['Button']

    if pressed == "Find Motor Zero":
      myStepper.zero()
    elif pressed == "Change Angle":
      myStepper.goAngle(angle)

except Exception as e:
  print(e)
  pass
GPIO.cleanup()