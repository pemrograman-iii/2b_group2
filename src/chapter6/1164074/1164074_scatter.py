import matplotlib.pyplot as plt

def datascatter():
    
    x = [1, 3, 5, 7, 9]
    y = [11, 13, 15, 17, 19]
    X = [1, 3, 5, 7, 9]
    Y = [12, 14, 16, 18, 20]
    
    for b in range (1, 5):
        plt.subplot(2, 2, b)
        plt.scatter(x, y, label = 'Data 1')
        plt.scatter(X, Y, label = 'Data 2')
        plt.xlabel('sumbu X')
        plt.ylabel('sumbu Y')
        plt.legend()
    plt.show()
datascatter()