# In[01]: Melakukan import pada module serial
import serial

# In[02]: Membuat fungsing mengambil data
def mengambilData():
    ser = serial.Serial('COM1',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

mengambilData()

# In[03]: Membuat file csv dai data arduino
import csv

def write():
    ser = serial.Serial('COM1',9600)
    with open('1164089.csv', mode='w') as csv_file:
        fieldnames = ['space']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'space': data})
            
write()
