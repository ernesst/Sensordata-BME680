#!/usr/bin/python
import time
import sys
import threading
import json
import urllib.request
import base64
import pprint
from datetime import datetime

start_time = time.time()
interval = 340 # set interval in seconds
url ='' # for example: https://YOUR-OWNCLOUD-INSTANCE/index.php/apps/sensorlogger/api/v1/createlog/ if you are using SensorLogger for owncloud
headers = {'content-type': 'application/json'}

# change this to match the location's pressure (hPa) at sea level


def sensorData():
 threading.Timer(interval, sensorData).start()
 cdatetime = datetime.now()
 currentDate = cdatetime.strftime('%Y-%m-%d %H:%M:%S')
 with open('/home/pi/ram/bme280.log', 'r') as f:
         lines = f.read().splitlines()
         last_line = lines[-1]
 AIQ = float(last_line.split()[1])
 temperature =  float(last_line.split()[5])
 humidity = float(last_line.split()[6])
 Pressure = float(last_line.split()[7])
 Resistance = float(last_line.split()[8])

 if humidity is not None and temperature is not None and AIQ is not None:
  payload0 = {
   'deviceId': 'Zero',
   'temperature': temperature,
   'humidity': humidity,
   'date': currentDate
   }

  payload1 = {
   'deviceId': '00A1',
   'date': currentDate,
   'data': [{'dataTypeId':'1',
            'value' : AIQ}
           ]
  }
  payload2 = {
   'deviceId': '00A2',
   'date': currentDate,
   'data': [{'dataTypeId':'2',
            'value' : Pressure}
           ]
  }

  payload3 = {
   'deviceId': '00A3',
   'date': currentDate,
   'data': [{'dataTypeId':'3',
            'value' : Resistance}
           ]
  }

  req = urllib.request.Request(url)
  base64string = base64.encodestring(('%s:%s' % ('login', 'Password')).encode()).decode().replace('\n', '') #add login and password for cloud instance
  req.add_header("Authorization", "Basic %s" % base64string)
  req.add_header("Content-Security-Policy", "default-src 'none';script-src 'self' 'unsafe-eval';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self';connect-src 'self';media-src 'self'")
  req.add_header('Content-Type','application/json')
  data0 = json.dumps(payload0)
  data1 = json.dumps(payload1)
  data2 = json.dumps(payload2)
  data3 = json.dumps(payload3)

  response0 = urllib.request.urlopen(req,data0.encode())
  response1 = urllib.request.urlopen(req,data1.encode())
  response2 = urllib.request.urlopen(req,data2.encode())
  response3 = urllib.request.urlopen(req,data3.encode())


 else:
  print('Failed to get reading. Try again!')
  sys.exit(1)

sensorData()
