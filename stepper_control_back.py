import RPi.GPIO as GPIO
from PCF import PCF8591
from stepper import Stepper
import time
import json
from urllib.request import urlopen
from urllib.parse import urlencode

api = "PWRX31PF18M31AG0"



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

params = {
    "api_key":api,
    1: Angle,
    2: Button,}
  params = urlencode(params)   # put dict data into a GET string

  # add "?" to URL and append with parameters in GET string:
  url = "https://api.thingspeak.com/update?" + params
  try:
    response = urlopen(url)      # open the URL to send the request
    print(response.status, response.reason)  # display the response
    print(response.read()) # display response page data
    time.sleep(16)    # 15 sec minimum
  except Exception as e:
    print(e)
GPIO.cleanup()