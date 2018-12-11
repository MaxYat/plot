import matplotlib.pyplot as plt
import numpy as np

from load_thaw_depth_probes import START_YEAR, FINISH_YEAR, load_data
probes, probes_by_year = load_data()

x = np.arange(START_YEAR, FINISH_YEAR+1)
# x = np.array(list(range(START_YEAR, FINISH_YEAR+1)))
# Задаём выборку из Гамма-распредления с параметрами формы=1. и масштаба=0.
# z = np.random.gamma(2., 1., N)
z = np.cos(x/10.)
z = np.array([])

# y = z.reshape(FINISH_YEAR-START_YEAR+1,-1)
y = z.reshape(10,-1)
#y = np.cos(y)

fig = plt.figure()
cc = plt.contourf(y)
cbar = plt.colorbar(cc)

plt.title('1. TITLE', color='green')
plt.xlabel('2. X - LABEL')
plt.ylabel('3. Y - LABEL', fontsize=16)

# Подписи для цветовых шкал
cbar.ax.set_xlabel('4. COLORBAR X-LABEL', color='b')
cbar.ax.set_ylabel('5. COLORBAR Y-LABEL', color='r')
plt.grid(True)

# смотри преамбулу
# save('pic_1_6_2', fmt='pdf')
# save('pic_1_6_2', fmt='png')

plt.show()