import csv

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    values = []
    for row in csv_reader:
        values.append(int(row[0]))
    values.sort()
    for i in range(len(values)):
        for j in range(1,len(values)):
            firsttwo = values[i] + values[j]
            diff = 2020 - firsttwo
            if diff in values:
                print(values[i], values[j], diff)
                print(values[i] * values[j] * diff)


    