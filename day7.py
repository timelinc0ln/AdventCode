import itertools

#def checkforvalue(dictlist, total, color):


BagData = open('bags.txt', 'r').read().split("\n")

allrules = {}
for line in BagData:
	#print(line)
	rule = line.split(' ')
	primarycolor = ''
	othercolors = []
	othercolor = ''
	for i in range(len(rule)):
		if i < 2:
			primarycolor += rule[i] # do nothing
		else:
			if rule[i] == 'contain' or 'bag' in rule[i] or rule[i].isnumeric() or rule[i] == 'no' or rule[i] == 'other':
				othercolors.append(othercolor)
				othercolor = ''
			else:
				othercolor += rule[i]
	while('' in othercolors):
		othercolors.remove('')
	allrules[primarycolor] = othercolors

value = ["shinygold"]
checkval = 0
while checkval < len(value):
	for i in allrules:
		for j in allrules[i]:
			if j in value and i not in value:
				value.append(i)
	checkval += 1

total = len(value) - 1  
print("Total combos:", total)

def process_keys(leftside):
	processleft = leftside.split(" ")
	processleft.remove("bags")
	processleft.remove("")
	leftvalue = processleft[0] + processleft[1]
	return leftvalue

def process_values(rightside):
	processright = rightside.split(" ")
	pairs = []
	for i in range(0, len(processright)):
		if processright[i].isnumeric():
			pair = (processright[i], processright[i+1] + processright[i+2])
			pairs.append(pair)
	return pairs


ruledictionary = {}
for line in BagData:
	leftside, rightside = line.split("contain")
	left = process_keys(leftside)
	right = process_values(rightside)
	ruledictionary[left] = right

def iterate()

value = ["shinygold"]
checkval = 0
count = 0
while checkval < len(value):
	for i in ruledictionary:
		#print(i)
		for j in ruledictionary[i]:
			#print(j[1])
			if j[1] in value and i not in value:
				#print(j[0])
				value.append(i)
				count += int(j[0])
	checkval += 1

print("Total bags:", count)