import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('ticks')
sns.set_palette('coolwarm')
i=0

folder = r'D:\RPM_Rapid\BrickworkPeriodDouble\AnalysedData'
for root, subpaths, files in os.walk(folder):
	if i == 0:
		subs = subpaths
		i+=1

count_list = []
for sub in subs:
	count_list.append(int(sub[-1]))
fig, ax = plt.subplots(1,1)
print(count_list)
print(len(count_list))
ax.hist(count_list, bins = [0.5,1.5,2.5,3.5,4.5, 5.5], rwidth = 0.8)
plt.show()