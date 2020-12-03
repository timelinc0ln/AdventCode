import csv

def istree(row, right, down, iterator):
	is_tree = False
	repeat_val = 31 - right
	if down == 1:
		if row[iterator] == '#':
			is_tree = True
		if iterator < repeat_val:
			iterator += right
		else:
			iterator -= repeat_val
	else:
		print("oh no")
	return is_tree, iterator

with open('slope.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	iterator = 0
	count = 0
	tree = False
	rowit = 0
	for row in csv_reader:
		if rowit % 2 != 0:
			print("Skipped row:", rowit)
		else:
			tree, iterator = istree(row[0], 1, 1, iterator)
			print(tree, iterator)
			if tree:
				count += 1
		rowit += 1
	print("Trees hit:", count)
	