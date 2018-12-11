import csv
import geopy.distance

START_YEAR = 1990
FINISH_YEAR = 2018


def convert_lat_long(degree):
    degree = degree.strip(',').\
        replace('\x94',"").replace('В',"").replace(",",".").replace("'", " ").replace("°", " ").\
        replace('”', " ").replace('"', " ").replace("  ", " ").strip()

    multiplier = 1 if degree[-1] in ['N', 'E'] else -1
    s = degree[:-1].strip().split(' ')
    return multiplier * sum(float(x) / 60 ** n for n, x in enumerate(s))


def parse_depth(depth):
    try:
        depth = float(depth.replace("*","").strip())
    except ValueError:
        depth = -1
    return depth


def limit(src_probes, min_dist, max_dist):
    result = []
    for probe in src_probes:
        if min_dist < probe[1] < max_dist:
            result.append(probe)
    return result


def load_data():

    file = open("data//CALM_Summary_table_utf8.csv")
    reader = csv.reader(file, delimiter = ';')

    probes = []

    for num, row in enumerate(reader):
        if num < 2:
            continue
        # if not row[1] in {"United States (Alaska)", "CANADA", "Russia"}:
        #     continue

        # if row[3].strip() in {"Tuymada (Yakutsk region)", "Junvvasshoe, Norway"}:
        #     continue

        if row[1] == "Central asia":
            break

        print(', '.join(row))
        lat = convert_lat_long(row[4])
        long = convert_lat_long(row[5])
        distance = geopy.distance.vincenty((lat, long), (90.0,0.0)).km
        print(distance)
        for year in range(START_YEAR, FINISH_YEAR+1):
            thaw_depth = parse_depth(row[year-START_YEAR+7])
            if thaw_depth < 0:
                continue
            probes.append((year, distance, thaw_depth))

    # probes.sort(key=attrgetter("min_time"))

    probes_by_year = {}

    for year in range(START_YEAR, FINISH_YEAR+1):
        probes_by_year[year] = []

    for probe in probes:
        probes_by_year[probe[0]].append((probe[1], probe[2]))

    return probes, probes_by_year

