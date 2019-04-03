# In[01]: Melakukan import module serial
import serial

# In[02]: Membuat fungsi looping atau pengulangan
def Looping():
    ser = serial.Serial('COM1',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
Looping()
