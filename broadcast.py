import serial
import requests
import ast
import time
ser = serial.Serial("/dev/serial0", 115200, timeout=1)
while 1:
	try:
		response = ser.readline()
		if response:
			gpsdata = ast.literal_eval(response)
			r = requests.post('https://mrgames-server.de/vehicle_safe/ServerScript.php', data = gpsdata )
			print r.text
	except KeyboardInterrupt:
		ser.close()
