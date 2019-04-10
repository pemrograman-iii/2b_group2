import matplotlib.pyplot as plt

def dataplot():
    
    x = [1, 3, 5, 7, 9]
    y = [11, 13, 15, 17, 19]
    X = [1, 3, 5, 7, 9]
    Y = [12, 14, 16, 18, 20]
    
    for a in range (1, 5):
        plt.subplot(2, 2, a)
        plt.plot(x, y, label = 'Data 1')
        plt.plot(X, Y, label = 'Data 2')
        plt.xlabel('sumbu X')
        plt.ylabel('sumbu Y')
        plt.legend()
    plt.show()
dataplot()
