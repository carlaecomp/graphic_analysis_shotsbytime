import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import collections
from operator import itemgetter

name = "128_nodes_model_v2"
ref_arquivo = open(name+".txt", "r")

data = {}

for linha in ref_arquivo:
    valores = linha.split()
    # print(valores)
    val1 = int(valores[7])
    if not(val1 in data):
        data[val1] = {}

    tam = len(data[val1])
    data[val1][tam] = valores[3]

ref_arquivo.close()

data_sum_ord = {}
for i in data:
      data_sum_ord[i] = sum([ float(x) for x in data[i].values() ])

data_sum_ord = sorted(data_sum_ord.items(),  key=itemgetter(1), reverse=True)

# print data_sum_ord

eixo_x = []

for i in data_sum_ord:
      eixo_x.append(i[0])

# data_ord = {}
data_ord = collections.OrderedDict()
for i in eixo_x:
      data_ord[str(i)] = data[i]

# print data_ord
data_inv = collections.OrderedDict()

# tam = len(data[0])
for i in data_ord:
    # print(i)
    # print(data[i])
    for j in data_ord[i]:
          # print(j)
          # print(data[i][j])
          # print("if")
          if not(j in data_inv):
              data_inv[j] = collections.OrderedDict()
          data_inv[int(j)][int(i)] = data_ord[i][j]
print "data_inv"
print eixo_x

# print eixo_x
# df = pd.DataFrame(data_inv)
# data_inv = {"zero": {30:5500}, 2: {'32':5500}}

df1 = pd.DataFrame(data_inv, index=eixo_x)
df = df1.astype(float)
# df.legend()
df.plot(kind="barh", stacked=True, figsize=(15, 7))
title =  name.replace('_', ' ').upper()
plt.title(title)
# xs = [i + 0.5 for i, _ in enumerate(eixo_x)]
# plt.bar(data_inv)

# plt.xticks([i + 0.5 for i, _ in enumerate(eixo_x)], eixo_x)

# plt.xticks(eixo_x)
# index = ['Diploma', 'Fail (Promoted)', 'HC','Bachelor']
# new_ticks = np.linspace(0, 1, 128)       # 0.0, 0.1, 0.2, ..., 1.0
# ax.set_xticks(new_ticks)
# positions of each tick, relative to the indices of the x-values
# ax.set_xticks(np.interp(new_ticks, df1.index, np.arange(df1.size)))

# labels
# ax.set_xticklabels(new_ticks)
plt.yticks(np.arange(0, 128, 5))
plt.legend(loc='best')
# plt.yticks(rotation=25, fontsize=5)
plt.show()
