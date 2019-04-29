# -*- coding: utf-8 -*-
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import collections
from operator import itemgetter
import sys

# Format the input file
# Time in seconds X Shoot Y Proce K
# Example of name = "128_nodes_model_v2"
name = sys.argv[1:][0]
# print name
ref_arquivo = open("data/"+name+".txt", "r")

# Read data from the file, the time from each shot from each node
data = {}
for linha in ref_arquivo:
    valores = linha.split()
    val1 = int(valores[7])
    if not(val1 in data):
        data[val1] = {}

    tam = len(data[val1])
    data[val1][tam] = valores[3]

size_nodes = len(data)
ref_arquivo.close()

# Order the nodes slowest to the fasts
data_sum_ord = {}
for i in data:
    data_sum_ord[i] = sum([float(x) for x in data[i].values()])

data_sum_ord = sorted(data_sum_ord.items(),  key=itemgetter(1), reverse=False)

# Organize from the graphic
eixo_x = []
for i in data_sum_ord:
    eixo_x.append(i[0])

data_ord = collections.OrderedDict()
for i in eixo_x:
    data_ord[str(i)] = data[i]

data_inv = collections.OrderedDict()

# Invert data from the graphic y=>nodes, x=>time
for i in data_ord:
    for j in data_ord[i]:
        if not(j in data_inv):
            data_inv[j] = collections.OrderedDict()
        data_inv[j][int(i)] = data_ord[i][j]

# Plot the graphic
df1 = pd.DataFrame(data_inv, index=eixo_x)
df = df1.astype(float)
lines= df.plot(kind="barh", stacked=True, figsize=(15, 7))
title = name.replace('_', ' ').upper()
plt.title(title)
plt.yticks(np.arange(0, size_nodes, 5))

legend_vector = []
for i in range(1, 10):
    legend_item = (str(i) + "\xBA shot").decode(encoding='latin-1')
    legend_vector.append(legend_item)
legend_vector.append("...")
plt.legend(legend_vector)
# plt.legend(loc='best')

plt.ylabel('Nodes')
plt.xlabel('Time (s)')
# plt.show()
plt.savefig("figures/"+name+'.png')
