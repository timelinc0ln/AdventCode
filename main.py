import csv

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    values = []
    for row in csv_reader:
        values.append(int(row[0]))
    values.sort()

    # find two numbers that sum to 2020
    for i in range(len(values)):
        for j in range(1,len(values)):
            total = values[i] + values[j]
            if total == 2020:
                print("Values are:", values[i], values[j])
                print("Product is:", values[i] * values[j])
                break

    # find three numbers that sum to 2020
    for i in range(len(values)):
        for j in range(1,len(values)):
            firsttwo = values[i] + values[j]
            diff = 2020 - firsttwo
            if diff in values:
                print("Values are:", values[i], values[j], diff)
                print("Product is:", values[i] * values[j] * diff)
                break


    