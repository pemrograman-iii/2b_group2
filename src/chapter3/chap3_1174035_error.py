def cekerror(NPM):
	try:
		a = int(NPM)
		a = a+1110
		print(str(a))
	except ValueError:
		print("Tidak boleh memakai huruf!!")