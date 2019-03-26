def npm(x):
    a = 0
    b = int(x[5:7])
    while a < b :
        a += 1
        print("Hello, " + x + " Apa Kabar?")
    return x

x = input("Masukkan NPM: ")
c = npm(x)