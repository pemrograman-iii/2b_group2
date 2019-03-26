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