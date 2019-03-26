# In[01]:
import csv

# In[02]:
with open('Datasetyn.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        print(row)

# In[03]:
with open('AnakKelas.csv', mode='w') as kelas_file:
    kelas_writer = csv.writer(kelas_file, delimiter=',', quotechar='"')
    kelas_writer.writerow(['Yusniar','D4 TI','3C'])
    kelas_writer.writerow(['Imron','D4 TI','3C'])
    kelas_writer.writerow(['Cokro','D4 TI','3C'])
    