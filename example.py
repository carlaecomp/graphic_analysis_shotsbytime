import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

grupos = 4
indice = np.arange(grupos)
dic = {'Chesterville': { 'Diploma': 5, 'Fail (Promoted)': 5, 'HC': 16,'Bachelor': 28},
     'Ebony Park': { 'Diploma': 3, 'Fail (Promoted)': 0, 'HC': 1, 'Bachelor': 1},
     'Makhaza': {'Diploma': 9, 'Fail (Promoted)': 13, 'HC': 4,'Bachelor': 15}}

index = ['Diploma', 'Fail (Promoted)', 'HC','Bachelor']
df = pd.DataFrame(dic, index=index)
print df.columns
df.plot(kind="barh", stacked=True)
# df.sort_values(by['Chesterville', 'Ebony Park', 'Makhaza'])
# df["columns"].value_counts().plot.barh(title="Nmero de apartamentos")
# plt.xticks(indice + 0.2, ('Diploma', 'Fail', 'HC', 'Bachelor')) 


plt.show()