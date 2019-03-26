class Fungsi:
	def __init__(self, NPM):
		self.NPM = NPM
	def Angka(self):
		NPM = int(self.NPM)
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

	def Nomor2(self):
		y = self.NPM[5:7]
		g = int(y)
		for i in range(g):
		    status = print('Halo ' + self.NPM,'Apa Kabar?')
		return status

	def Nomor3(self):
		y = self.NPM[4:7]
		x = self.NPM[4:5]
		y = self.NPM[5:6]
		z = self.NPM[6:7]
		g = (int(x) + int(y) + int(z))
		for i in range(g):
		    status = print('Halo ' + y,'Apa Kabar?')
		return status

	def Nomor4(self):
		y = self.NPM[4:5]
		print('Halo ' + y,'Apa Kabar?')
		return

	def Nomor5(self):
		NPM = list(self.NPM)
		for x in NPM:
			print(x)

	def Nomor6(self):
		NPM = list(self.NPM)
		bnyk = 0
		for x in NPM:
			bnyk= bnyk+int(x)
		print("Hasilnya : " +str(bnyk))

	def Nomor7(self):
		NPM = list(self.NPM)
		bnyk = 0
		for x in NPM:
			bnyk= bnyk*int(x)
		print("Hasilnya : " +str(bnyk))

	def Nomor8(self):
		NPM = list(self.NPM)
		for x in NPM:
		    if int(x) != 0:
		    	if int(x)%2==0:
		            print(x, end = "")

	def Nomor9(self):
		NPM = list(self.NPM)
		for x in NPM:
		    if int(x) != 0:
		    	if int(x)%2==1:
		            print(x, end = "")

	def BilPrima(self):
	    NPM = list(self.NPM)
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

