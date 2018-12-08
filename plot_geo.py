import csv
import geopy.distance

def convert(degree):
    degree = degree.strip(',').\
        replace('\x94',"").replace(","," ").replace("'", " ").replace("°", " ").replace('"', " ").replace("  ", " ").strip()

    multiplier = 1 if degree[-1] in ['N', 'E'] else -1
    s = degree[:-1].strip().split(' ')
    return multiplier * sum(float(x) / 60 ** n for n, x in enumerate(s))

file = open("data//CALM_Summary_table_utf8.csv")
reader = csv.reader(file, delimiter = ';')

for row in reader:
    if not row[1] in {"United States (Alaska)", "CANADA", "Russia"}:
        continue
    print(', '.join(row))
    lat = convert(row[4])
    long = convert(row[5])
    print(geopy.distance.vincenty((lat, long), (90.0,0.0)).km)
    # for x in range(7, )

