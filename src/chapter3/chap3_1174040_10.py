def BilPrima(NPM):
    NPM = list(NPM)
    for x in NPM:
        if int(x) != 0:
            i = 1
            bil = 0
            while i <= int(x):
                if int(x)%i==0:
                    bil+=1
                i+=1
            if bil == 2:
                print(x)