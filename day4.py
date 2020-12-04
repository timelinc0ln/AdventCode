import csv

def is_whitespace(line):
    return line.isspace()

class Passport:
	def __init__(self='', byr='', iyr='', eyr='', hgt='', hcl='', ecl='', pid='', cid=''):
		self.byr = byr
		self.iyr = iyr
		self.eyr = eyr
		self.hgt = hgt
		self.hcl = hcl
		self.ecl = ecl
		self.pid = pid
		self.cid = cid
	
	def __str__(self):
		return "byr: %s, iyr: %s, eyr: %s, hgt: %s, hcl: %s, ecl: %s, pid: %s, cid: %s" % (self.byr,
			self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid, self.cid)
	
	def is_valid_byr(self):
		if len(self.byr) != 4 or (int(self.byr) < 1920 or int(self.byr) > 2002):
			return False
		else:
			return True
	
	def is_valid_iyr(self):
		if len(self.iyr) != 4 or (int(self.iyr) < 2010 or int(self.iyr) > 2020):
			return False
		else:
			return True
	
	def is_valid_eyr(self):
		if len(self.eyr) != 4 or (int(self.eyr) < 2020 or int(self.iyr) > 2030):
			return False
		else: 
			return True

	def is_valid_hgt(self):
		if self.hgt == '' or len(self.hgt) < 4: # doesn't have in or cm in the height value
			return False
		else:
			if 'c' in self.hgt:
				value = self.hgt.split('c')
				height = int(value[0])
				if height < 150 or height > 193:
					return False
				else:
					return True
			if 'i' in self.hgt:
				value = self.hgt.split('i')
				height = int(value[0])
				if height < 59 or height > 76:
					return False
				else: 
					return True

	def is_valid_hcl(self):
		if self.hcl == '':
			return False
		if self.hcl[0] != '#' or len(self.hcl) != 7:
			return False
		else:
			return True

	def is_valid_ecl(self):
		valideyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if self.ecl in valideyecolors:
			return True
		else:
			return False

	def is_valid_pid(self):
		if len(self.pid) != 9:
			return False
		else:
			return True


PassportData = open('passports.csv', 'r').read().split("\n\n")

PassportList = []
for passport in PassportData:
	values = passport.split('\n')
	newpass = Passport()
	for value in values:
		segment = value.split(' ')
		for item in segment:
			testval = item.split(':')
			if testval[0] == 'byr':
				newpass.byr = testval[1]
			if testval[0] == 'iyr':
				newpass.iyr = testval[1]
			if testval[0] == 'eyr':
				newpass.eyr = testval[1]
			if testval[0] == 'hgt':
				newpass.hgt = testval[1]
			if testval[0] == 'hcl':
				newpass.hcl = testval[1]
			if testval[0] == 'pid':
				newpass.pid = testval[1]
			if testval[0] == 'ecl':
				newpass.ecl = testval[1]
			if testval[0] == 'cid':
				newpass.cid = testval[1]
	PassportList.append(newpass)

validpassports = len(PassportList)
print("Total passports:", validpassports)
for passport in PassportList:
	if passport.byr == '' or passport.iyr == '' or passport.eyr == '' or passport.hgt == '' or passport.hcl == '' or passport.ecl == '' or passport.pid == '':
		validpassports -= 1
print("Valid passports (no cid):", validpassports)

validpassports2 = len(PassportList)
print("Total passports:", validpassports2)
for passport in PassportList:
	input("")
	print(passport)
	if passport.is_valid_byr() and passport.is_valid_iyr() and passport.is_valid_eyr() 	and passport.is_valid_hgt() and passport.is_valid_hcl() and passport.is_valid_ecl()	and passport.is_valid_pid():
		print("Valid Passport")
	else:
		validpassports2 -= 1
		print("Invalid Passport")
print("Total valid passports(all criteria):", validpassports2)