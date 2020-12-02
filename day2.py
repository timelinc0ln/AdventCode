import csv

alpha = ['nope','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def parser(line):
	strpw = line[0]
	splitpw = strpw.split()
	rep = splitpw[0]
	letters = splitpw[1]
	pw = splitpw[2]
	letterclean = letters[0]
	limits = rep.split('-')
	lowerlimit = limits[0]
	upperlimit = limits[1]
	count = 0;
	for letter in range(len(pw)):
		if pw[letter] == letterclean:
			count += 1
	if (count >= int(lowerlimit)) & (count <= int(upperlimit)):
		return True
	else:
		return False

def parser2(line):
	strpw = line[0]
	splitpw = strpw.split()
	rep = splitpw[0]
	letters = splitpw[1]
	pw = splitpw[2]
	letterclean = letters[0]
	limits = rep.split('-')
	lowerlimit = int(limits[0])
	upperlimit = int(limits[1])
	if (pw[lowerlimit-1] == letterclean) ^ (pw[upperlimit-1] == letterclean):
		return True
	else:		
		return False

with open('passwords.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	numvalid = 0
	numvalid2 = 0
	for row in csv_reader:
		if parser(row):
			numvalid += 1
		if parser2(row):
			numvalid2 += 1
	print("Valid Passwords (policy 1):", numvalid)
	print("Valid Passwords (policy 2):", numvalid2)
