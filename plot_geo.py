import matplotlib.pyplot as plt
from colour import Color

from load_thaw_depth_probes import START_YEAR, FINISH_YEAR, load_data

probes, probes_by_year = load_data()

red = Color("red")
colors = list(red.range_to(Color("green"),FINISH_YEAR-START_YEAR+1))

fig = plt.figure()
legend = []

for year in range(2010, FINISH_YEAR+1): # range(START_YEAR, FINISH_YEAR+1,3):
    # year = FINISH_YEAR - _year + START_YEAR

    probes_by_year[year].sort(key=lambda data: data[0])

    x = []
    y = []

    for data in probes_by_year[year]:
        if data[0] < 1800 or data[0] > 3500:
            continue
        x.append(data[0])
        y.append(data[1])

    legend.append(year)
    p = plt.plot(x, y, color = colors[year-START_YEAR].get_hex_l(), label=year)

plt.legend(legend)
# plt.savefig('filename.png', dpi=300)
plt.show()
