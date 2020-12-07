AnswerData = open('answers.csv', 'r').read().split("\n\n")

def check_list(value, list):
	for each in list:
		if value not in each:
			return False
	return True

possibleanswer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answerlist =[]
for answer in AnswerData:
	value = answer.split('\n')
	answerlist.append(value)

count = 0

grouplist = []
for group in answerlist:
	blankstring = ""
	for item in group:
		blankstring += item
	grouplist.append(blankstring)

for group in grouplist:
	for letter in possibleanswer:
		if letter in group:
			count += 1
		
print("Yes answer:", count)

count2 = 0

for group in answerlist:
	for letter in possibleanswer:
		if check_list(letter, group):
			count2 += 1

print("All yes:", count2)