import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

folder = r'D:\RPM_Rapid\SquarePeriodDouble'
file = r'PeriodicityAll4.npz'
filename = os.path.join(folder, file)
npzfile = np.load(filename)


print(npzfile['arr_0'])
print(npzfile['arr_1'].mean())
print(npzfile['arr_2'])
print(npzfile['arr_3'])


def periodAnalysisPlot(folder, name = 'PeriodicityAll5.npz'):
	npzfile = np.load(os.path.join(folder, name))
	period_array = npzfile['arr_0']
	QD_array = npzfile['arr_1']
	width_array = npzfile['arr_2']
	count_array = npzfile['arr_3']
	period_list = period_array.tolist()
	period_list = [0 if x is None else x for x in period_list]
	period_array = np.array(period_list)
	#print(period_array.tolist())
	#print(width_array[np.where(period_array==0)], QD_array[np.where(period_array==0)], count_array[np.where(period_array==0)])

	fig, ax = plt.subplots(1,1)
	total = period_array.size
	bin_number = np.ceil(np.sqrt(total))//2*2+1
	bins = np.linspace(-.5,15, num = 17)
	print(period_array.tolist())
	ax.hist(period_array,log=True, normed =True,bins=bins, alpha=1, label = 'Period of Memory', rwidth = 0.8)
	ax.set_xlabel('Period')
	ax.set_ylabel('Probability of occurring')

	fig, ax = plt.subplots(1,1)
	total = period_array.size
	bin_number = np.ceil(np.sqrt(total))//2*2+1
	bins = np.linspace(-0.5,15, num = 7)
	print(period_array.tolist())
	ax.hist(period_array,log=True, bins=bins, alpha=1, label = 'Period of Memory', rwidth = 0.8)
	ax.set_xlabel('Period')
	ax.set_ylabel('Number of occurrences')
	
	data_dict = {'version':count_array,'QD':QD_array*100, 'Width':width_array*1e-9, 'Count': period_array}

	data_df = pd.DataFrame(data_dict)
	grouped = data_df.groupby('version')

	data = data_df.groupby(by=['Width', 'QD']).mean()
	piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)

	plt.figure()
	yticks = piv.index.values.round(2).tolist()[::4]
	ax = sns.heatmap(piv,vmin=0, vmax=6, square = True, yticklabels = yticks[::1],cbar_kws={'label': 'Average period of lattice'}, cmap = 'Blues',  xticklabels=4)
	ax.set_yticks(np.array(yticks)*ax.get_ylim()[1]/10.)
	ax.invert_yaxis()
	plt.tight_layout()
	ax.set_ylabel('Quenched Disorder (%)')
	ax.set_xlabel('Width (nm)')
	plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
	plt.setp(ax.get_yticklabels(), rotation=0, verticalalignment='top')

	for vers, group in grouped:
		print(vers)
		data = group.groupby(by=['Width', 'QD']).mean()
		piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)
		plt.figure()
		print(piv.index.values.round(2))
		print(list(piv.index.values.round(2))[::4])
		print(piv.index.values.round(2).tolist()[::4])
		yticks = piv.index.values.round(2).tolist()[::4]
		ax = sns.heatmap(piv,vmin=0, vmax=6, square = True, yticklabels = yticks[::1],cbar_kws={'label': 'Average period of lattice'}, cmap = 'Blues',  xticklabels=4)
		ax.set_yticks(np.array(yticks)*ax.get_ylim()[1]/10.)
		ax.invert_yaxis()
		plt.tight_layout()
		ax.set_ylabel('Quenched Disorder (%)')
		ax.set_xlabel('Width (nm)')
		plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
		plt.setp(ax.get_yticklabels(), rotation=0, verticalalignment='top')


#periodAnalysisPlot(folder, file)
#plt.show()


def TcyclesPlot(folder, name = 'PeriodicityAll5.npz'):
	npzfile = np.load(os.path.join(folder, name))
	period_array = npzfile['arr_0']
	QD_array = npzfile['arr_1']
	width_array = npzfile['arr_2']
	count_array = npzfile['arr_3']
	period_list = period_array.tolist()
	period_list = [-100 if x is None else x for x in period_list]
	period_array = np.array(period_list)
	data_dict = {'version':count_array,'QD':QD_array/0.1, 'Width':width_array, 'Count': period_array}

	data_df = pd.DataFrame(data_dict)
	grouped = data_df.groupby('version')

	data = data_df.groupby(by=['Width', 'QD']).mean()
	piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)
	#print(pd.crosstab(data.QD, data.Width))
	plt.figure()
	print(piv.index.values.round(2))
	print(list(piv.index.values.round(2))[::4])
	print(piv.index.values.round(2).tolist()[::4])
	yticks = piv.index.values.round(2).tolist()[::4]
	#yticklabels=piv.index.values.round(2).tolist()[::4]
	ax = sns.heatmap(piv,vmin=0, vmax=6, square = True, yticklabels = yticks[::1],cbar_kws={'label': 'Average period of lattice'}, cmap = 'Blues',  xticklabels=4)
	#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
	ax.set_yticks(np.array(yticks)*ax.get_ylim()[1]/10.)
	#ax.set_yticks(np.array(piv.index.values.round(2).tolist()[::4]))
	#ax.set_yticklabels(piv.index.values.round(2).tolist()[::4])
	ax.invert_yaxis()
	plt.tight_layout()
	#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
	#plt.locator_params(nbins=6)
	#ax.yaxis.set_major_locator(plt.MaxNLocator(5))
	ax.set_ylabel('Quenched Disorder (%)')
	ax.set_xlabel('Width (nm)')
	plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
	plt.setp(ax.get_yticklabels(), rotation=0, verticalalignment='top')

folder= r'D:\RPM_Rapid\SquarePeriodDouble'
file = r'PeriodicityAll4.npz'
TcyclesPlot(folder, file)
plt.show()