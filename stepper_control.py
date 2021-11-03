#!/usr/bin/cgipython1

import cgi
import json
import cgitb
cgitb.enable()


print("Content-type: text/html\n\n")
data= cgi.FieldStorage()
s1 = data.getvalue('Angle')
s2 = data.getvalue('Button')
data = {"Angle":s1,"Button":s2}
with open('angle.txt', 'w') as f:
  json.dump(data,f)

print('<html>')
print('<form action="/cgi-bin/stepper_control.py" method="POST">')
print('<input type="text" name="Angle"> <br>')
print('<input type="submit" name="Button" value="Find Motor Zero"> <br>')
print('<input type="submit" name="Button" value="Change Angle">')
print('</form>')
print('</html>')