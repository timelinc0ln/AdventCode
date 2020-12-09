instructions = open('instructions2.txt', 'r').read().split("\n")

def parseline(line):
	values = line.split(' ')
	op = values[0]
	num = 0
	if values[1][0] == '+':
		num = int(values[1][1:len(values[1])])
	else:
		num = int(values[1][1:len(values[1])]) * -1
	return (op, num)

def determinecount(instructionlist):
	i = 0
	count = 0
	itracker = []

	while i < len(instructionlist):
		itracker.append(i)
		if instructionlist[i][0] == 'acc':
			count += instructionlist[i][1]
			i += 1
		elif instructionlist[i][0] == 'jmp':
			i += instructionlist[i][1]
			if i in itracker:
				break
		else:
			i += 1
	print("Total accumulated:", count)

def finderror(instructionlist):
	i = 0
	count = 0
	itracker = []

	while i < len(instructionlist):
		itracker.append(i)
		if instructionlist[i][0] == 'acc':
			count += instructionlist[i][1]
			i += 1
		elif instructionlist[i][0] == 'jmp':
			j = i
			i += instructionlist[i][1]
			if i in itracker:
				print(j)
				print(instructionlist[j][0])
				break
		else:
			i += 1
	print(count)

instructionlist = []

for line in instructions:
	instructionlist.append(parseline(line))

determinecount(instructionlist)
finderror(instructionlist)