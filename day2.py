def parser(line):
	print line
	
with open('passwords.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

for row in csv_reader:
	parser(row)