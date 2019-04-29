import json
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Format the input file
# Time in seconds X Shoot Y Proce K
# Example of name = "128_nodes_model_v2"

name = sys.argv[1:][0]
ref_arquivo = open("data/"+name+".txt", "r")

x = {}

for linha in ref_arquivo:
    valores = linha.split()
    val1 = int(valores[7])
    if not(val1 in x):
		x[val1] = []

    x[val1].append(valores[3])

ref_arquivo.close()

x_sort = sorted(x)
ref_arquivo = open("data_output/" + name+".txt","w")

tam = len(x[val1])
for indices in x_sort:
    ref_arquivo.write(str(indices)+'	')
    for i in range(0, tam):
    	ref_arquivo.write(x[indices][i]+'	')
    ref_arquivo.write('\n')


ref_arquivo.write('\n')
for i in range(0, tam):
    for indices in x_sort:
    	ref_arquivo.write(x[indices][i]+'	')
    ref_arquivo.write('\n')
ref_arquivo.close()