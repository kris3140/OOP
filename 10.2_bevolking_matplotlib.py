import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pandas as pd
import numpy as np

data = pd.read_csv('bevolking.csv', sep=";", index_col=0)
data_vl = data.loc["Vlaanderen", :]

women_vl = data_vl[data_vl["Gender"] == 'Women']
women_vl_pop = list(women_vl.loc[: , "Population"])     # [630037, 1976581, 752827]

men_vl = data_vl[data_vl["Gender"] == 'Men']
men_vl_pop = list(men_vl.loc[: , "Population"])     # [659950, 2009936, 623731]


age_groups = list(np.unique(data_vl["Age Group"]))     # ['18-', '18-64', '65+']
x = np.arange(len(age_groups))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_vl_pop, width, label='Men', color='#301ee3')
rects2 = ax.bar(x + width/2, women_vl_pop, width, label='Women', color='#b0f68e')

ax.set_ylabel('Aantal')
plt.subplots_adjust(left=0.2)
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
ax.set_title('Bevolking Vlaanderen op 01/01/2021')
ax.set_xticks(x, age_groups)
ax.legend()
plt.show()



# data
#            Age Group Gender  Population
# Region
# Vlaanderen       18-  Women      630037
# Vlaanderen       18-    Men      659950
# Vlaanderen     18-64  Women     1976581
# Vlaanderen     18-64    Men     2009936
# Vlaanderen       65+  Women      752827
# Vlaanderen       65+    Men      623731
# Brussel          18-  Women      134558
# Brussel          18-    Men      140995
# Brussel        18-64  Women      392440
# Brussel        18-64    Men      392951
# Brussel          65+  Women       93898
# Brussel          65+    Men       65128
# Wallonie         18-  Women      365068
# Wallonie         18-    Men      381514
# Wallonie       18-64  Women     1103755
# Wallonie       18-64    Men     1104332
# Wallonie         65+  Women      394863
# Wallonie         65+    Men      298674
