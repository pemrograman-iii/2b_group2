##File 3lib.py##
def nomorsatu(NPM):	
	NPM = int(NPM)
	char = "#"
	if NPM%3==0:
		char = "*"
	if NPM%3==1:
		char = "#"
	if NPM%3==2:
		char = "+"
	line = []
	line.append(" ##         ##      ########     ##    ##       #####       #######     ########")
	line.append("####       ####      ##    ##    ##    ##      ##   ##     ##     ##    ##      ")
	line.append("  ##         ##          ##      ##    ##     ##     ##           ##    ##      ")
	line.append("  ##         ##         ##       ##    ##     ##     ##     #######     ####### ")
	line.append("  ##         ##        ##        #########    ##     ##           ##          ##")
	line.append("  ##         ##        ##              ##      ##   ##     ##     ##    ##    ##")
	line.append("######     ######      ##              ##       #####       #######      ###### ")
	a=0
	for x in line:
		print(line[a].replace("#", char))
		a+=1
	return

def nomordua(NPM):
	print("Input : "+NPM)
	x=1
	print("Output : ")
	while x <= 87:
		x+=1
		print("Halo, "+NPM+" apa kabar?")
	return

def nomortiga(NPM):
	print("Input : "+NPM)	
	jumlah = len(NPM)
	a = int(NPM[jumlah-3])
	b = int(NPM[jumlah-2])
	c = int(NPM[jumlah-1])
	x=1
	while x <= (a+b+c):
		print("Output : "+NPM[jumlah-3:])
		x+=1
	return

def nomorempat(NPM):
	print("Input : "+NPM)
	jumlah = len(NPM)
	print("Output : ")
	print("Halo, "+NPM[jumlah-3]+" apa kabar?")
	return

def nomorlima(NPM):
	NPM = list(NPM)
	for x in NPM:
		print(x)
	return

def nomorenam(NPM):
	NPM = list(NPM)
	jum = 0
	for x in NPM:
		jum+=int(x)
	print("Hasil : "+str(jum))
	return

def nomortujuh(NPM):
	NPM = list(NPM)
	jum = 1
	for x in NPM:
		jum*=int(x)
	print("Hasil : "+str(jum))
	return

def nomordelapan(NPM):
	NPM = list(NPM)
	for x in NPM:
		if int(x)!=0:
			if int(x)%2==0:
				print(x, end="")
	return

def nomorsembilan(NPM):	
	NPM = list(NPM)
	for x in NPM:
		if int(x)!=0:
			if int(x)%2==1:
				print(x, end = "")
	return

def nomorsepuluh(NPM):
	NPM = list(NPM)
	for x in NPM:
		if int(x)!=0:
			i = 1
			bil = 0
			while i <= int(x):
				if int(x)%i==0:
					bil+=1
				i+=1
			if bil == 2:
				print(x)
	return