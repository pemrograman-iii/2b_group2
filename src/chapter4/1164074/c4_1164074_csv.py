# In[1]
import csv

def rdcsv():
    with open('1164074_csv.csv') as r:
        read = csv.reader(r)
        lst = list(read)
        print(lst)

# In[2]
def dctcsv():
    
    with open('1164074_csv.csv') as bk:
        r = csv.DictReader(bk)
        l = list(r)
        print(l)

# In[3]
def wrtcsv():
    with open('1164074_csvW.csv', 'w') as csvw:
        data = csv.writer(csvw, delimiter=',')
        data.writerow(['D1', 'D2', '22/02/2002'])
        
def rdcsv2():
    with open('1164074_csvW.csv') as r:
        read = csv.reader(r)
        lst = list(read)
        print(lst)


