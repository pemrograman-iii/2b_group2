# In[01] Melakukan import pada module serial
import serial

# In[02]: Membuat Fungsi menggunakan Pyserial
def Arduino():
    ser = serial.Serial(110200)
    print(ser.name)
    
Arduino()