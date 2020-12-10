numbers = open('input.txt', 'r').read().split("\n")


def gathersums(list):
	sumlist = []
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			value = list[i] + list[j]
			sumlist.append(value)
	return sumlist



numberlist = []
for line in numbers:
	numberlist.append(int(line))

# subset the list	
front = 0
back = 5
allpossiblevalues = []
while back < len(numberlist) + 1:
	temp = numberlist[front:back]
	possiblevalues = gathersums(temp)
	allpossiblevalues.append(possiblevalues)
	front += 1
	back +=1
	
subsetpossible = allpossiblevalues[5:]
subsetproposed = numberlist[5:]

for i in range(len(subsetproposed)): #15
	print(i)
	for j in range(len(subsetpossible)): # 11
		if i > len(subsetpossible):
			if subsetproposed[i] not in subsetpossible[len(subsetpossible)-1]:
				print("found error:", subsetpossible[i])
				print(subsetpossible[len(subsetpossible)-1])
		else:
			if subsetproposed[i] not in subsetpossible[j]: 
				print("found error:", subsetproposed[i])
				print(subsetpossible[j])

