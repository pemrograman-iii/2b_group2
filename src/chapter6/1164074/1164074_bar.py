import matplotlib.pyplot as plt

def databar():

    for i in range (1, 5):
        plt.subplot(2, 2, i)
        plt.bar(['DOTA 2'], ['0'], label = "MOBA",
                color = 'r')
        plt.bar(['PUBG'], ['199000'], label = "Battleroyal",
                color = 'y')
        plt.bar(['CSGO'], ['199000'], label = "FPP",
                color = 'b')
        plt.bar(['RDR2'], ['780000'], label = "Adventure",
                color = 'g')
        plt.legend()
        plt.xlabel('Game')
        plt.ylabel('Harga')
        plt.title('Harga Game tahun 2018')
    plt.show()
databar()