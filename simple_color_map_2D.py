import matplotlib.pyplot as plt
# plt.style.use('classic')

import numpy as np

x = np.linspace(0, 10, 1000)
# I = np.sin(x) * np.cos(x[:, np.newaxis])
I = np.sin(x) + np.cos(x[:, np.newaxis])
# I = x * x[:, np.newaxis]

plt.imshow(I)
plt.colorbar()
plt.show()