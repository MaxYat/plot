import csv

file = open("data\CALM_Summary_table.csv")
reader = csv.reader(file, delimiter = ';')

row_num = 0
for row in reader:
    print(', '.join(row))
    row_num += 1
    if row_num <= 2: continue
    lat = row[4]
    long = row[5]
    # for x in range(7, )

