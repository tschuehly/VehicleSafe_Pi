import serial
import requests
import ast
import time
ser = serial.Serial("/dev/serial0", 9600, timeout=1)
print "started"
while 1:
	try:
		response = ser.readline()
		if response and '{' in response and '}' in response:
			try:
				response = response.split("{")[1]
				response = "{" + response
				gpsdata = ast.literal_eval(response)
			except ValueError as e:
				print e
			r = requests.post('https://mrgames-server.de/vehicle_safe/ServerScript.php', data = gpsdata )
			print r.text
			print "gpsdata received"
		if response and '#' in response:
			print "# received"
			ser.write('1')
			time.sleep(2)
	except KeyboardInterrupt:
		ser.close()
