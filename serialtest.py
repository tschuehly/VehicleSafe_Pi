import serial
ser = serial.Serial("/dev/serial0", 115200, timeout=1)

#ser.write("testing")
try:
	while 1:
		#ser.write(raw_input())
		response = ser.readline()
		#print repr(response)
		if response:
			print response
except KeyboardInterrupt:
	ser.close()
