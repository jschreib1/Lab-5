import RPi.GPIO as GPIO
from PCF import PCF8591
from stepper import Stepper
import time
import json
from urllib.request import urlopen
from urllib.parse import urlencode

api = "PWRX31PF18M31AG0"

#print("11")

try:
  while True:
    myStepper = Stepper(0x48)
    #print("hello")
    with open("angle.txt", 'r') as f:
      data = json.load(f)
      print(data)
    angle = data['Angle']
    pressed = data['Button']

    if pressed == "Find Motor Zero":
      myStepper.zero()
    elif pressed == "Change Angle":
      myStepper.goAngle(int(angle))
    

except Exception as e:
  print(e)
  pass
GPIO.cleanup()