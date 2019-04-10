import matplotlib.pyplot as plt

def datapie():
    
    x = [25, 15, 25, 35]
    y = ['PUBG', 'CSGO', 'DOTA 2', 'APEX LEGEND']
    c = ['y','b','r','g']
    for i in range(1, 5):
        plt.subplot(2,2,i)
        plt.pie(x,
        labels = y,
        colors = c,
        startangle=90,
        shadow= True,
        explode=(0, 0, 0, 0.2),
        autopct='%1.0f%%')        
        plt.subplots_adjust(hspace=.4)
    plt.show()
datapie()