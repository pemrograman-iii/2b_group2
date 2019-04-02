import serial

def tryARD():
    set = serial.Serial("COM4", 9600)
    print(set.name)

tryARD()