import RPi.GPIO as GPIO
from PCF import PCF8591



try:
  myADC = PCF8591(0x48)
  myStepper = Stepper(pins)
  light_level = myStepper.getval()
  myStepper.zero(light_level)
  #myStepper.goAngle(90)

except Exception as e:
  print(e)
  pass
GPIO.cleanup()