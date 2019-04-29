import json
import pandas as pd
import matplotlib.pyplot as plt

ref_arquivo = open("128v2.txt","r")

x = {}

for linha in ref_arquivo:
    valores = linha.split()
    # print(valores)
    val1 = int(valores[7])
    if not(val1 in x):
		x[val1] = []

    x[val1].append(valores[3])
    
# print(x)

# print(json.dumps(x))

ref_arquivo.close()
x_sort = sorted(x)
ref_arquivo = open("dataprc.txt","w")
# print(json.dumps(x_sort))
tam = len(x[val1])
for indices in x_sort:
    ref_arquivo.write(str(indices)+'	')
    for i in range(0, tam):
    	ref_arquivo.write(x[indices][i]+'	')
    ref_arquivo.write('\n')

# dic = {}
# key = ''

# for m in x:
#     for p in x_sort:
#         if p in m:
#             key = m
#             dic[key] = []
#             break
#     if m != key:
#         dic[key].append(m)

# print(dic)

ref_arquivo.write('\n')
for i in range(0, tam):
    for indices in x_sort:
    	ref_arquivo.write(x[indices][i]+'	')
    ref_arquivo.write('\n')
ref_arquivo.close()
# for time in x[indices]:
# print(time)

# dic = {'Chesterville': {'Bachelor': 8, 'Diploma': 5, 'Fail (Promoted)': 5, 'HC': 16},
#      'Ebony Park': {'Bachelor': 1, 'Diploma': 3, 'Fail (Promoted)': 0, 'HC': 1},
#      'Makhaza': {'Bachelor': 15, 'Diploma': 9, 'Fail (Promoted)': 13, 'HC': 4}}

# df = pd.DataFrame(dic)

# df.plot(kind="bar", stacked=True)
# plt.show()

# df = pd.DataFrame(dic)

# df.plot(kind="bar", stacked=True)
# plt.show()