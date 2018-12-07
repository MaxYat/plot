import matplotlib.pyplot as plt
import numpy as np

lag = 0.1

# d = [678002.1706658392, 6305543.573574919, 677269.1018910082, 6305356.248197533, 677218.4233807817, 6305374.9355972875, 677218.4233807817, 6305374.9355972875, 677184.551699229, 6305332.925595277, 677191.3845292934, 6305382.468551225, 677153.0724092722, 6305389.767746384, 677053.4836493825, 6305306.51408876, 677080.5061595691, 6305291.032719974, 677113.2833489394, 6305254.218123345, 677166.7284173785, 6305197.751881656, 677238.405169558, 6305200.798810269, 677203.7513191607, 6305152.7368504, 677203.4961930865, 6305068.242211764, 677069.460730633, 6305085.618228144, 677016.0886449282, 6305075.6610960625, 677016.0886449282, 6305075.6610960625, 677090.9650586118, 6305134.234868399, 677051.4119229489, 6305135.3411748875, 677021.2844986406, 6305160.365302152, 676984.3827222154, 6305123.622956897, 676984.3827222154, 6305123.622956897, 676952.6086044292, 6305124.012790194, 676921.4607906995, 6305173.380809315, 677006.2925325291, 6305220.082057128, 677006.2925325291, 6305220.082057128, 677040.6758558322, 6305247.232800916, 677025.2279015032, 6305274.552177499, 677003.2127517192, 6305310.297439478, 676950.2814424997, 6305328.858951792, 676887.0851164657, 6305337.823828141, 676961.5603067649, 6305301.496091498, 677001.3228899471, 6305488.08971346, 677012.8763286675, 6305539.515730919, 676957.0953089931, 6305471.38818149, 676875.7741513302, 6305487.106924425, 676920.991893769, 6305546.64865523, 676860.2216942078, 6305557.221373987, 676868.4885100478, 6305590.886289561, 676716.2970870584, 6305629.848973412, 676846.3612550014, 6305741.4268832775, 678002.1706658392, 6305543.573574919]

d = [678002.1706658392, 6305543.573574919, 678086.7860457335, 6305475.030302024, 678164.4592678307, 6305454.832040542, 678308.9327432775, 6305448.860947613, 678536.5556118973, 6305341.261058531, 678362.9384678056, 6305302.597882591, 678311.9193812903, 6305262.140452951, 678353.0406304795, 6305217.399356098, 678365.2535150291, 6305209.963799399, 678298.9755910276, 6305053.539333239, 678363.5216988568, 6305033.228657447, 678284.615374313, 6304915.274651576, 678223.2968492716, 6304872.79589291, 678200.6322238154, 6304883.58740145, 678165.9908456933, 6304884.608389228, 678236.3212376122, 6304812.22888275, 678315.2819718784, 6304800.781418484, 678281.8673158151, 6304684.216440113, 678162.9463345974, 6304694.402711048, 678043.0301458598, 6304662.41891343, 678041.37856786, 6304765.446531378, 678041.37856786, 6304765.446531378, 678077.1862256455, 6304771.739298418, 678121.8201900593, 6304828.82439386, 678141.7807509771, 6304829.588076446, 678114.4952130516, 6304895.965882193, 678117.2127107597, 6304925.517649297, 677959.6606005931, 6304830.058078376, 677765.6029939081, 6304839.835210651, 677782.2325819142, 6304938.180711637, 677829.2365510843, 6304970.758137531, 677859.9058797578, 6304961.099097907, 677870.6885176394, 6304939.947578863, 677868.4334457947, 6304935.83890511, 677887.7091365742, 6304926.306970159, 677959.2456041266, 6304929.906158034, 677919.7262935594, 6304994.536495022, 677909.8577904748, 6304993.691798404, 677901.868456917, 6305026.654294382, 677825.7969252552, 6305075.0133546125, 677968.7100744069, 6305131.602258113, 677985.6703732956, 6305048.142549513, 678037.1696393354, 6305036.887309904, 678012.4816808528, 6305009.8536844, 678034.2059361377, 6304997.7519997135, 678098.4886991289, 6304982.441607436, 678127.1414416945, 6305045.290719707, 678222.1850103165, 6305072.469249869, 678252.8946702906, 6305091.582083739, 678220.5872854518, 6305096.843646435, 678214.3115954819, 6305558.389915305, 678206.6049283706, 6305523.555077872, 678002.1706658392, 6305543.573574919]

x = []
y = []

for i in range(len(d)):
    if i & 1 == 0:
        x.append(d[i])
    else:
        y.append(d[i])

roads = [(676757.5878067396, 6305496.805485147, 676991.5403290752, 6305439.525343599), (676991.5403290752, 6305439.525343599, 677116.776743448, 6305413.414414426), (677116.776743448, 6305413.414414426, 677140.8474228776, 6305410.201957546), (677140.8474228776, 6305410.201957546, 677290.4532716719, 6305414.110492042), (677290.4532716719, 6305414.110492042, 677333.922320673, 6305415.62524055), (677333.922320673, 6305415.62524055, 677487.1755273612, 6305419.91892532), (677487.1755273612, 6305419.91892532, 677688.5256928636, 6305424.596444153), (677688.5256928636, 6305424.596444153, 677810.0331416064, 6305431.672745791), (677810.0331416064, 6305431.672745791, 677882.6947700747, 6305444.46979588), (676547.5986371395, 6305722.184726762, 676676.7833406061, 6305700.575293861), (676676.7833406061, 6305700.575293861, 676747.0912911661, 6305688.17540601), (676747.0912911661, 6305688.17540601, 677036.8084853983, 6305638.7249344615), (677036.8084853983, 6305638.7249344615, 677166.0617075674, 6305612.786432721), (677166.0617075674, 6305612.786432721, 677184.0380306353, 6305606.4173816405), (677184.0380306353, 6305606.4173816405, 677319.2392974098, 6305577.058296084), (677319.2392974098, 6305577.058296084, 677365.2947959458, 6305566.534745131), (677365.2947959458, 6305566.534745131, 677464.5288895596, 6305543.11743782), (677464.5288895596, 6305543.11743782, 677585.1240984497, 6305518.494789138), (677585.1240984497, 6305518.494789138, 677703.4436574315, 6305491.437915236), (677703.4436574315, 6305491.437915236, 677721.9075603775, 6305487.9897695165), (677721.9075603775, 6305487.9897695165, 677805.6302466632, 6305469.046018547), (677805.6302466632, 6305469.046018547, 677979.9049819498, 6305430.006064212), (677979.9049819498, 6305430.006064212, 678217.0200665318, 6305377.943904474), (678217.0200665318, 6305377.943904474, 678364.138790996, 6305345.894993139), (678364.138790996, 6305345.894993139, 678482.0173408913, 6305308.029231704), (678482.0173408913, 6305308.029231704, 678462.56875277, 6305077.704003317), (677407.0101032115, 6305838.703942389, 677349.684702892, 6305586.155597067), (677349.684702892, 6305586.155597067, 677343.7288139366, 6305556.8120242385), (677343.7288139366, 6305556.8120242385, 677316.9213360378, 6305430.617345308), (677316.9213360378, 6305430.617345308, 677311.4797005504, 6305403.524860019), (677311.4797005504, 6305403.524860019, 677241.6196827254, 6305030.407416368), (677241.6196827254, 6305030.407416368, 677242.8647875228, 6304998.249502259), (677242.8647875228, 6304998.249502259, 677175.1011164908, 6304050.779316649), (676743.1376066131, 6306003.0927805, 676707.6524914661, 6305721.2772299), (676707.6524914661, 6305721.2772299, 676703.222228462, 6305686.0923628025), (676703.222228462, 6305686.0923628025, 676683.6427342433, 6305567.56532378), (676568.3907906874, 6305695.4246147, 676757.5878067396, 6305496.805485147), (678462.56875277, 6305077.704003317, 678420.9208667312, 6304902.269510841), (678420.9208667312, 6304902.269510841, 678261.4049184804, 6304484.054995988), (678261.4049184804, 6304484.054995988, 678228.1279710446, 6304375.298693212), (678462.56875277, 6305077.704003317, 678490.9973615177, 6305055.514883078), (678490.9973615177, 6305055.514883078, 678820.6597173389, 6304842.489825459), (678820.6597173389, 6304842.489825459, 678842.1723897082, 6304830.706302125), (678842.1723897082, 6304830.706302125, 679162.6577073939, 6304621.770869062), (679162.6577073939, 6304621.770869062, 679179.8133700597, 6304607.684012278), (679179.8133700597, 6304607.684012278, 679483.6165225501, 6304412.544128904), (679483.6165225501, 6304412.544128904, 679553.255996286, 6304376.754293342), (679608.4876571519, 6305029.836457622, 679385.1636947998, 6304504.831422627), (679212.5703245105, 6303899.430817904, 679290.4637380788, 6304022.7090082), (679290.4637380788, 6304022.7090082, 679495.265361754, 6304339.147758337), (679495.265361754, 6304339.147758337, 679527.840807643, 6304389.703906728)]

# x = np.arange(0.0, 2*np.pi+lag, lag)
# y = np.cos(x)

fig = plt.figure()
plt.plot(x, y)

for road in roads:
    rx = [road[0],road[2]]
    ry = [road[1],road[3]]
    plt.plot(rx, ry, color="red")

plt.text(np.pi-0.5, 0,  '1 Axes', fontsize=26, bbox=dict(edgecolor='w', color='w'))
plt.text(0.1, 0, '3 Yaxis', fontsize=18, bbox=dict(edgecolor='w', color='w'), rotation=90)
plt.text(5, -0.9, '2 Xaxis', fontsize=18, bbox=dict(edgecolor='w', color='w'))

plt.title('1a TITLE')
plt.ylabel('3a Ylabel')
plt.xlabel('2a Xlabel ')

plt.text(5, 0.85, '6 Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)
plt.text(0.95, -0.55, '6 Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)

plt.text(5.75, -0.5, '7 Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))
plt.text(0.15, 0.475, '7 Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))

plt.grid(True)

# смотри преамбулу
# save('pic_1_5_1', fmt='pdf')
# save('pic_1_5_1', fmt='png')

plt.show()