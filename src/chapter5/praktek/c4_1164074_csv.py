import csv

def rCSV():	
	with open('1164074_try.csv', 'r') as f:
		read = csv.reader(f)
		lst = list(read)
	return lst