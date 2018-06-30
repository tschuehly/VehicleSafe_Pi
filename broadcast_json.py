import serial
import requests
import json
import time
import os
ser = serial.Serial("/dev/serial0", 9600, timeout=1)
print "started"
while 1:
	try:
		response = ser.readline()
		if response and '{' in response and '}' in response:
			print repr(response)
			response_json = response
			response_json = response_json.replace("'", "\"")
			response_json = response_json.replace("\x00", "")
			response_json = response_json.split("{")[1]
			response_json = "{" + response_json
			print "response: " + response_json
			gpsdata = json.loads(response_json)
			print gpsdata
			r = requests.post('https://mrgames-server.de/vehicle_safe/ServerScript.php', data = gpsdata )
			print r.text
			print "gpsdata received"
		if response and '#' in response:
			print "# received"
			ser.write('1')
			time.sleep(2)
		if response and 'shutdown' in response:
			print "shutdown received"
			ser.close()
			os.system("sudo shutdown -h now")
			sys.exit()
	except KeyboardInterrupt:
		ser.close()
