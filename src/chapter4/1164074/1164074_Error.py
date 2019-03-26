# In[1]
import pandas as bear
def TryExcept():
    try:
        coba3 = bear.read_csv('1164074_pandas.csv', parse_dates={'tanggal':[0, 1]})
        print(coba3)
    except SyntaxError:
        print("nilai eror cuy")

# In[2]: Solusi

coba3 = bear.read_csv('1164074_pandas.csv', parse_dates=['tanggal'])
print(coba3)
