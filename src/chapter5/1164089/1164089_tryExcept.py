# In[01]: Melakukan import modul serial
import serial

# In[02]: Membuat fungsi trxEcept
def teError():
    try:
        ser = serial.Serial('COM1',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan Dalam Penulisan Syntax") 
        
teError()