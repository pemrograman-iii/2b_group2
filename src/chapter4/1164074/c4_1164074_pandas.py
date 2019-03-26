# In[1]
import pandas as bear
coba = bear.read_csv('1164074_pandas.csv')
    
# In[2]
coba2 = bear.read_csv('1164074_pandas.csv')
form = coba2.to_dict(orient='records')
    
# In[3]
coba3 = bear.read_csv('1164074_pandas.csv', parse_dates=['tanggal'])
print(coba3)
    
# In[4]
coba4 = bear.read_csv('1164074_pandas.csv')
coba4.set_index('nama')
    
# In[6]
coba5 = bear.read_csv('1164074_pandas.csv', header=0, names=['Nama', 'Tanggal Lahir', 'Program Studi', 'Kelas', 'Alamat Mahasiswa', 'IPK Mahasiswa'])
print(coba5)

# In[7]

def wrtcsv():
    with open('1164074_pandas.csv') as opn:
        run = bear.read_csv(opn)
        run.to_csv('1164074_pandasW.csv')
        
def rdcsv():
    with open('1164074_pandasW.csv') as opn:
        go = bear.read_csv(opn)
        print(go)
    