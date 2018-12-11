import matplotlib.pyplot as plt
import numpy as np
from colour import Color

from load_thaw_depth_probes import START_YEAR, FINISH_YEAR, load_data, limit
probes, probes_by_year = load_data()

probes = limit(probes, 0, 4000)

min_depth = min(probes, key=lambda x:x[2])[2]
max_depth = max(probes, key=lambda x:x[2])[2]

red = Color("green")
colors = list(red.range_to(Color("red"),256))

plt.figure(dpi=600)

probes.sort(key=lambda x:x[2], reverse=True)

for probe in probes:
    alert = (probe[2]-min_depth)/(max_depth-min_depth)
    plt.plot(probe[0], probe[1], '.', markersize=1+round(alert*15),
             color = colors[round(alert*255)].get_hex_l()
             )

# plt.colorbar()
plt.show()