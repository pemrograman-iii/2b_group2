def Angka(NPM):
	NPM = int(NPM)
	char = "#"
	if NPM%3 == 0:
	    char = "*"
	if NPM%3 == 1:
	    char = "#"
	if NPM%3 == 2:
	    char = "+"
	row = []
	row.append("   ##      ##   ######## ##          #####   ##          #####")   
	row.append(" ####    ####   ##    ## ##    ##   ##   ##  ##    ##   ##   ##")  
	row.append("   ##      ##       ##   ##    ##  ##     ## ##    ##  ##     ##") 
	row.append("   ##      ##      ##    ##    ##  ##     ## ##    ##  ##     ##") 
	row.append("   ##      ##     ##     ######### ##     ## ######### ##     ##") 
	row.append("   ##      ##     ##           ##   ##   ##        ##   ##   ## ") 
	row.append(" ######  ######   ##           ##    #####         ##    #####  ")
	a = 0
	for x in row:
	    print(row[a].replace("#", char))
	    a+=1

def Nomor2(NPM):
	y = NPM[5:7]
	g = int(y)
	for i in range(g):
	    status = print('Halo ' + NPM,'Apa Kabar?')
	return status

def Nomor3(NPM):
	y = NPM[4:7]
	x = NPM[4:5]
	y = NPM[5:6]
	z = NPM[6:7]
	g = (int(x) + int(y) + int(z))
	for i in range(g):
	    status = print('Halo ' + y,'Apa Kabar?')
	return status

def Nomor4(NPM):
	y = NPM[4:5]
	print('Halo ' + y,'Apa Kabar?')
	return

def Nomor5(NPM):
	NPM = list(NPM)
	for x in NPM:
		print(x)

def Nomor6(NPM):
	NPM = list(NPM)
	bnyk = 0
	for x in NPM:
		bnyk= bnyk+int(x)
	print("Hasilnya : " +str(bnyk))

def Nomor7(NPM):
	NPM = list(NPM)
	bnyk = 0
	for x in NPM:
		bnyk= bnyk*int(x)
	print("Hasilnya : " +str(bnyk))

def Nomor8(NPM):
	NPM = list(NPM)
	for x in NPM:
	    if int(x) != 0:
	    	if int(x)%2==0:
	            print(x, end = "")

def Nomor9(NPM):
	NPM = list(NPM)
	for x in NPM:
	    if int(x) != 0:
	    	if int(x)%2==1:
	            print(x, end = "")

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

