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