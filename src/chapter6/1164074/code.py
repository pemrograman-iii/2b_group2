# In[1]
# Garis
import matplotlib.pyplot as plt

x = (2, 4, 8, 10, 12)
y = (4, 8, 12, 16, 20)
plt.plot(x, y)
plt.show()

# In[2]
# Titik
plt.scatter(x,y)
plt.show()

# In[3]
# Batang
b=[2,4,6,3,50,100,5,7,81,42,99,80]
num_bins = 3
n, bins, patches = plt.hist(b, num_bins, facecolor = 'blue')
plt.show()

# In[5]
# Pie
labels = 'Travel', 'Main Game', 'Makan', 'Membaca'
sizes = [5, 35, 30, 30]
explode = (0, 0.1, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.0f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 

plt.show()

# In[6]
# Legend
plt.plot([1, 2, 3])
plt.legend (['garis simple'])


# In[7]
# Label
plt.plot([1, 2, 3])
plt.ylabel('nilai Y')
plt.xlabel('nilai X')

# In[8]
# Subplot
plt.subplot(3, 3, 1)
plt.plot(x, y)

plt.subplot(3, 3, 2)
plt.plot(x, y)

plt.subplot(3, 3, 3)
plt.plot(x, y)

plt.subplot(3, 3, 4)
plt.plot(x, y)

plt.subplot(3, 3, 5)
plt.plot(x, y)

plt.subplot(3, 3, 6)
plt.plot(x, y)

plt.subplot(3, 3, 7)
plt.plot(x, y)

plt.subplot(3, 3, 8)
plt.plot(x, y)

plt.subplot(3, 3, 9)
plt.plot(x, y)

# In[9]
# Hist
x = [27, 28, 29, 30, 90, 91, 92, 93, 150, 151, 152, 153]
nK = 5
plt.hist(x, nK, facecolor='blue', alpha=0.5)
plt.show()

# In[10]
# 