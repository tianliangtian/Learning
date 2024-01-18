import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = []
df1.append(pd.read_excel(r"./data_set/new1_1.xlsx"))
df1.append(pd.read_excel(r"./data_set/new1_2.xlsx"))
df1.append(pd.read_excel(r"./data_set/new1_3.xlsx"))
df1.append(pd.read_excel(r"./data_set/new1_4.xlsx"))
df1.append(pd.read_excel(r"./data_set/new1_5.xlsx"))
Fre_name = df1[0].columns[0]
Amp_name = df1[0].columns[1]
Fre = df1[0][Fre_name]
Amp = []
for i in np.arange(0,len(df1[0][Fre_name])):
    Amp.append(0)
    for j in np.arange(0, 5):
        Amp[i] += df1[j][Amp_name][i]
    
    Amp[i] /= 5

fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
ax.set_xlim([0, 5000])
line1 = ax.plot(Fre, Amp)
ax.set_xlabel(Fre_name)
ax.set_ylabel(Amp_name)
fig.suptitle('FFT for one weight')
plt.show()