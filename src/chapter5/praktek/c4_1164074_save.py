import serial

def rSerialLoop():
	ser = serial.Serial('COM3', 9600, timeout=2)
	lst = []
	while True:
		x = ser.readline()
		if x:
			print(x)
			lst.append(x)
		else:
			break
	return lst