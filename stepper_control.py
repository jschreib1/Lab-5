#!/usr/bin/cgipython1

import cgi
import json
import cgitb
from urllib.request import urlopen
from urllib.parse import urlencode
import time
cgitb.enable()
api = "PWRX31PF18M31AG0"

print("Content-type: text/html\n\n")
data= cgi.FieldStorage()
s1 = data.getvalue('Angle')
s2 = data.getvalue('Button')
data = {"Angle":s1,"Button":s2}
with open('angle.txt', 'w') as f:
  json.dump(data,f)

#params stuff
while True:
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

print('<html>')
print('<form action="/cgi-bin/stepper_control.py" method="POST">')
print('<input type="text" name="Angle"> <br>')
print('<input type="submit" name="Button" value="Find Motor Zero"> <br>')
print('<input type="submit" name="Button" value="Change Angle">')
print('</form>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1539967/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1539967/widgets/375909"></iframe>')
print('</html>')