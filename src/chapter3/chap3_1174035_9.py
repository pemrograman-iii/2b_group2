def nomorsembilan(NPM):
	NPM = list(NPM)
	for x in NPM:
		if int(x)!=0:
			if int(x)%2==1:
				print(x, end = "")
	return