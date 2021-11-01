#!/usr/bin/cgipython1

import cgi
import json
import cgitb
cgitb.enable()


print("Content-type: text/html\n\n")
data= cgi.FieldStorage()
s1 = data.getvalue('slider1')
data = {"slider1":s1}
with open('angle.txt', 'w') as f:
  json.dump(data,f)