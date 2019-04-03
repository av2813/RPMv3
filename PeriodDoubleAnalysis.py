import rpmClass_Stable as rpm
import numpy as np
import math
import os
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pandas as pd
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)
sns.set_style("ticks")
sns.set_palette("bright")


Lattice = rpm.ASI_RPM(1, 1)

#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width4.200000e-07_Count3'
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width3.800000e-07_Count5'
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD8.000002e-02_Width2.600000e-07_Count1'
#folder= r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD6.400004e-02_Width3.400000e-07_Count3'


#The folder with all the data in it
#folder = r'D:\RPM_Rapid\SquarePeriodDouble'
#folder = r'D:\RPM_Rapid\SquarePeriodDouble'
folder = r'D:\RPM_Rapid\SizeDependence'
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width4.200000e-07_Count3'	#period 2
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.000000e-01_Width2.600000e-07_Count2' #period 4
#folder = r'D:\RPM_Rapid\SquarePeriodDouble\PeriodDoublingData_QD1.200009e-02_Width6.000000e-08_Count2'	#period 3




'''
#Lattice.identifyRPMchain(folder)
for root, subs, files in os.walk(folder):
	for sub in subs:
		if 'PeriodDoublingData' in sub:
			
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			print(path)
			file_count = len(fi)
			print(file_count)
			if file_count > 45 and 'AnalysedData' not in path:
				Lattice.identifyRPMchain(path)
'''


'''
tcycle_list = []
QD_list = []
width_list = []
count_list = []
for root, subs, files in os.walk(folder):
	for sub in subs:
		if 'PeriodDoublingData' in sub:
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			print(path)
			file_count = len(fi)
			print(file_count)
			if file_count > 45 and 'AnalysedData' not in path:
				tcycle_list.append(Lattice.trainingCycles(path))
				QD_list.append(float(Lattice.sortFunc(sub, '_QD', '_Width', False)))
				width_list.append(float(Lattice.sortFunc(sub, '_Width', '_Count', False)))
				count_list.append(Lattice.sortFunc(sub, '_Count', ''))#count_list.append(Lattice.sortFunc(sub, 'Count', ''))
temp_var1 = np.array(tcycle_list)
temp_var2 = np.array(QD_list)
temp_var3 = np.array(width_list)
temp_var4  = np.array(count_list)
print(np.unique(temp_var2, True, True, True))
np.savez_compressed(os.path.join(folder, 'TrainingCyclesAll2'), temp_var1, temp_var2, temp_var3, temp_var4)
'''

def periodAnalysis(folder, checkstring = 'PeriodDouble', var1_checkstr = ['_init', '_Size'], var2_checkstr = ['_Size', '_n'],\
					count_strcheck = ['_n', '']):
	period_list = []
	var1_list = []
	var2_list = []
	count_list = []
	for root, subs, files in os.walk(folder):
		for sub in subs:
			if checkstring in sub:
				path, dirs, fi = next(os.walk(os.path.join(root, sub)))
				print(path)
				file_count = len(fi)
				print(file_count)
				if file_count > 45 and 'AnalysedData' not in path:
					period_list.append(Lattice.determinePeriod(path))
					var1_list.append(str(Lattice.sortFunc(sub, var1_checkstr[0], var1_checkstr[1], False)))
					var2_list.append(Lattice.sortFunc(sub, var2_checkstr[0], var2_checkstr[1]))
					count_list.append(Lattice.sortFunc(sub, count_strcheck[0], count_strcheck[1]))#count_list.append(Lattice.sortFunc(sub, 'Count', ''))
	temp_var1 = np.array(period_list)
	temp_var2 = np.array(var1_list)
	temp_var3 = np.array(var2_list)
	temp_var4  = np.array(count_list)
	np.savez_compressed(os.path.join(folder, 'PeriodicityAll5'), temp_var1, temp_var2, temp_var3, temp_var4)

def periodAnalysisPlot(folder, name = 'PeriodicityAll5.npz'):
	npzfile = np.load(os.path.join(folder, name))
	period_array = npzfile['arr_0']
	var1_array = npzfile['arr_1']
	var2_array = npzfile['arr_2']
	count_array = npzfile['arr_3']
	period_list = period_array.tolist()
	period_list = [0 if x is None else x for x in period_list]
	period_array = np.array(period_list)
	print(period_array.tolist())
	print(width_array[np.where(period_array==0)], QD_array[np.where(period_array==0)], count_array[np.where(period_array==0)])

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



	plt.show()
'''
period_list = []
initstate_list = []
size_list = []
count_list = []
for root, subs, files in os.walk(folder):
	for sub in subs:
		if 'Square_' in sub:
			
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			print(path)
			file_count = len(fi)
			print(file_count)
			if file_count > 45 and 'AnalysedData' not in path:
				period_list.append(Lattice.determinePeriod(path))
				initstate_list.append(str(Lattice.sortFunc(sub, '_init', '_Size', False)))
				size_list.append(Lattice.sortFunc(sub, '_Size', '_n'))
				count_list.append(Lattice.sortFunc(sub, '_n', ''))#count_list.append(Lattice.sortFunc(sub, 'Count', ''))
temp_var1 = np.array(period_list)
temp_var2 = np.array(initstate_list)
temp_var3 = np.array(size_list)
temp_var4  = np.array(count_list)
print(np.unique(temp_var2, True, True, True))
np.savez_compressed(os.path.join(folder, 'PeriodicityAll4'), temp_var1, temp_var2, temp_var3, temp_var4)
'''
'''
npzfile = np.load(os.path.join(folder, 'TrainingCyclesAll2.npz'))

period_array = npzfile['arr_0']
width_array = npzfile['arr_1']
QD_array = npzfile['arr_2']
count_array = npzfile['arr_3']
period_list = period_array.tolist()
period_list = [0 if x is None else x for x in period_list]
period_array = np.array(period_list)
print(period_array.tolist())
print(width_array[np.where(period_array==0)], QD_array[np.where(period_array==0)], count_array[np.where(period_array==0)])

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
bins = np.linspace(0.5,6.5, num = 7)
print(period_array.tolist())
ax.hist(period_array,log=True, bins=bins, alpha=1, label = 'Period of Memory', rwidth = 0.8)

ax.set_xlabel('Period')
ax.set_ylabel('Number of occurrences')
plt.show()

data_dict = {'version':count_array,'QD':QD_array*100, 'Width':width_array*1e-9, 'Count': period_array}

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

plt.show()
for vers, group in grouped:
	print(vers)
	data = group.groupby(by=['Width', 'QD']).mean()
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



plt.show()
'''

################################################################################

'''
data_group =data_df.groupby(by = ['QD', 'Width']).mean()
print(data_group)
#for name, group in data_group:
#	print(name)
#	print(group.mean())
data = data_df.groupby(['QD', 'Width', 'version']).mean()
#new_data = data_df.groupby(['QD']).mean().groupby(['Width']).mean()
#print(data_df)
#print(perioddouble)
#plt.figure()
#plt.scatter(np.array(width)*1000, np.array(QD)*1000, c = np.array(count))
#plt.xlabel('Interaction Strength (mT)')
#plt.ylabel('Quenched disorder')
#plt.colorbar()
#sns.set_context('poster', font_scale = 2)
print(data)
piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)
#print(pd.crosstab(data.QD, data.Width))
plt.figure()
print(piv.index.values.round(2))
print(list(piv.index.values.round(2))[::4])
print(piv.index.values.round(2).tolist()[::4])
yticks = piv.index.values.round(2).tolist()[::4]
#yticklabels=piv.index.values.round(2).tolist()[::4]
ax = sns.heatmap(piv, square = True, yticklabels = yticks[::1],cbar_kws={'label': 'Percentage of period doubled spins'}, cmap = 'Blues',  xticklabels=4)
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

plt.show()

#######################################################################################################################
'''


'''
field0pPos_total = np.array([])
field1pPos_total = np.array([])
field2pPos_total = np.array([])
field0pNeg_total = np.array([])
field1pNeg_total = np.array([])
field2pNeg_total = np.array([])

monopole0pPos_total = np.array([])
monopole1pPos_total = np.array([])
monopole2pPos_total = np.array([])
monopole0pNeg_total = np.array([])
monopole1pNeg_total = np.array([])
monopole2pNeg_total = np.array([])

RPM_info_list = []

for root, subs, files in os.walk(folder):
	for sub in subs:
		if 'Square_' in sub:
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			file_count = len(fi)
			if file_count > 240:
				savefolder = folder + '\\AnalysedData4\\' + sub
				if not os.path.exists(savefolder):
					os.makedirs(savefolder)
				field1p_pos,field2p_pos,field0p_pos,field1p_neg,field2p_neg,field0p_neg,monopole1p_pos,monopole2p_pos,monopole0p_pos,monopole1p_neg,monopole2p_neg,monopole0p_neg = Lattice.monopoleDensityRPM(path, n=1)
				field0pPos_total = np.append(field0pPos_total, field0p_pos)
				field1pPos_total = np.append(field1pPos_total, field1p_pos)
				field2pPos_total = np.append(field2pPos_total, field2p_pos)
				field0pNeg_total = np.append(field0pNeg_total, field0p_neg)
				field1pNeg_total = np.append(field1pNeg_total, field1p_neg)
				field2pNeg_total = np.append(field2pNeg_total, field2p_neg)

				monopole0pPos_total = np.append(monopole0pPos_total, monopole0p_pos)
				monopole1pPos_total = np.append(monopole1pPos_total, monopole1p_pos)
				monopole2pPos_total = np.append(monopole2pPos_total, monopole2p_pos)
				monopole0pNeg_total = np.append(monopole0pNeg_total, monopole0p_neg)
				monopole1pNeg_total = np.append(monopole1pNeg_total, monopole1p_neg)
				monopole2pNeg_total = np.append(monopole2pNeg_total, monopole2p_neg)
				width = Lattice.returnWidth()
				QD = float(Lattice.sortFunc(sub, 'QD', '_Width', integer =False))
				count = Lattice.sortFunc(sub, 'Count', '')
				RPM_info_list.append([width, QD, count, field0p_pos, field1p_pos,field2p_pos,field0p_neg, field1p_neg,field2p_neg,monopole0p_pos, monopole1p_pos,monopole2p_pos,monopole0p_neg, monopole1p_neg,monopole2p_neg])
				print(field1p_pos,field2p_pos,field0p_pos,field1p_neg,field2p_neg,field0p_neg,monopole1p_pos,monopole2p_pos,monopole0p_pos,monopole1p_neg,monopole2p_neg,monopole0p_neg)
				#plt.close('all')

np.savez_compressed(os.path.join(folder, 'PeriodDoubleLF3'),field0pPos_total,field1pPos_total,field2pPos_total,field0pNeg_total,field1pNeg_total,field2pNeg_total)
np.savez_compressed(os.path.join(folder, 'PeriodDoubleMonopole3'),monopole0pPos_total,monopole1pPos_total,monopole2pPos_total,monopole0pNeg_total,monopole1pNeg_total,monopole2pNeg_total)
'''


'''
npzfile = np.load(os.path.join(folder,'PeriodDoubleLF3.npz'))
print(npzfile)
field0pPos_total = npzfile['arr_0']
field1pPos_total = npzfile['arr_1']
field2pPos_total = npzfile['arr_2']
field0pNeg_total = npzfile['arr_3']
field1pNeg_total = npzfile['arr_4']
field2pNeg_total = npzfile['arr_5']
print(field0pPos_total,field1pPos_total,field2pPos_total,field0pNeg_total,field1pNeg_total,field2pNeg_total)
fieldPos = np.append(field0pPos_total,field1pPos_total)
fieldPos = np.append(fieldPos,field2pPos_total)
fieldNeg = np.append(field0pNeg_total,field1pNeg_total)
fieldNeg = np.append(fieldNeg,field2pNeg_total)

fig1, ax1 = plt.subplots(1, 1)
total = fieldPos.size
bin_number = np.ceil(np.sqrt(total))//2*2+1
bins = np.linspace(min(fieldPos),max(fieldPos), num = bin_number)
#ax.hist(coer, bins=bins, alpha=0.5, label = 'all')

ax1.hist(field0pPos_total, bins=bins, alpha=0.5, label = '0Hz')
ax1.hist(field1pPos_total, bins=bins, alpha=0.5, label = '1Hz')
ax1.hist(field2pPos_total, bins=bins, alpha=0.5, label = '0.5Hz')
ax1.set_ylabel('Count')
ax1.set_xlabel('Local field (mT)')
plt.legend()

fig2, ax2 = plt.subplots(1, 1)
total = fieldNeg.size
bin_number = np.ceil(np.sqrt(total))//2*2+1
bins = np.linspace(min(fieldNeg),max(fieldNeg), num = bin_number)

ax2.hist(field0pNeg_total, bins=bins, alpha=0.5, label = '0Hz')
ax2.hist(field1pNeg_total, bins=bins, alpha=0.5, label = '1Hz')
ax2.hist(field2pNeg_total, bins=bins, alpha=0.5, label = '0.5Hz')

#fit_hist = mlab.normpdf(bins, mu, sigma)
#l = plt.plot(bins, fit_hist, 'r--', linewidth=2)

ax2.set_ylabel('Count')
ax2.set_xlabel('Local field (mT)')
plt.legend()
plt.show()


npzfile = np.load(os.path.join(folder, 'PeriodDoubleMonopole3.npz'))
monopole0pPos_total = npzfile['arr_0']
monopole1pPos_total = npzfile['arr_1']
monopole2pPos_total = npzfile['arr_2']
monopole0pNeg_total = npzfile['arr_3']
monopole1pNeg_total = npzfile['arr_4']
monopole2pNeg_total = npzfile['arr_5']

monopolePos = np.append(monopole0pPos_total,monopole1pPos_total)
monopolePos = np.append(monopolePos,monopole2pPos_total)
monopoleNeg = np.append(monopole0pNeg_total,monopole1pNeg_total)
monopoleNeg = np.append(monopoleNeg,monopole2pNeg_total)

fig1, ax1 = plt.subplots(1, 1)
total = monopolePos.size
bin_number = np.ceil(np.sqrt(total))//2*2+1
bins = np.linspace(min(monopolePos),max(monopolePos), num = bin_number)
#ax.hist(coer, bins=bins, alpha=0.5, label = 'all')

ax1.hist(monopole0pPos_total, bins=bins, alpha=0.5, label = '0Hz')
ax1.hist(monopole1pPos_total+0.05, bins=bins, alpha=0.5, label = '1Hz')
ax1.hist(monopole2pPos_total+0.1, bins=bins, alpha=0.5, label = '0.5Hz')
ax1.set_ylabel('Count')
ax1.set_xlabel('Monopole density')
plt.legend()

fig2, ax2 = plt.subplots(1, 1)
total = monopoleNeg.size
bin_number = np.ceil(np.sqrt(total))//2*2+1
bins = np.linspace(min(monopoleNeg),max(monopoleNeg), num = bin_number)

ax2.hist(monopole0pNeg_total, bins=bins, alpha=0.5, label = '0Hz')
ax2.hist(monopole1pNeg_total+0.05, bins=bins, alpha=0.5, label = '1Hz')
ax2.hist(monopole2pNeg_total+0.1, bins=bins, alpha=0.5, label = '0.5Hz')

#fit_hist = mlab.normpdf(bins, mu, sigma)
#l = plt.plot(bins, fit_hist, 'r--', linewidth=2)

ax2.set_ylabel('Count')
ax2.set_xlabel('Monopole density')
plt.legend()
plt.show()
'''


'''
coer0pPos_total = np.array([])
coer1pPos_total = np.array([])
coer2pPos_total = np.array([])
coer0pNeg_total = np.array([])
coer1pNeg_total = np.array([])
coer2pNeg_total = np.array([])

for root, subs, files in os.walk(folder):
	for sub in subs:
		if 'Square_' in sub:
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			file_count = len(fi)
			if file_count > 45:
				savefolder = folder + '\\AnalysedData4\\' + sub
				if not os.path.exists(savefolder):
					os.makedirs(savefolder)
				coer0p_pos, coer1p_pos, coer2p_pos, coer0p_neg, coer1p_neg, coer2p_neg = Lattice.periodDoubleHistogram(path, savefolder = savefolder)
				coer0pPos_total = np.append(coer0pPos_total, coer0p_pos)
				coer1pPos_total = np.append(coer1pPos_total, coer1p_pos)
				coer2pPos_total = np.append(coer2pPos_total, coer2p_pos)
				coer0pNeg_total = np.append(coer0pNeg_total, coer0p_neg)
				coer1pNeg_total = np.append(coer1pNeg_total, coer1p_neg)
				coer2pNeg_total = np.append(coer2pNeg_total, coer2p_neg)
				plt.close('all')

np.savez_compressed(os.path.join(folder, 'PeriodDoubleHc'),coer0pPos_total,coer1pPos_total,coer2pPos_total,coer0pNeg_total,coer1pNeg_total,coer2pNeg_total)
coerPos = np.append(coer0pPos_total, coer1pPos_total)
coerPos = np.append(coerPos, coer2pPos_total)

coerNeg = np.append(coer0pNeg_total, coer1pNeg_total)
coerNeg = np.append(coerNeg, coer2pNeg_total)

fig1, ax1 = plt.subplots(1, 1)
total = coerPos.size
bin_number = np.ceil(np.sqrt(total))//2*2+1
bins = np.linspace(min(coerPos),max(coerPos), num = bin_number)
#ax.hist(coer, bins=bins, alpha=0.5, label = 'all')

ax1.hist(coer0pPos_total, bins=bins, alpha=0.5, label = '0Hz')
ax1.hist(coer1pPos_total, bins=bins, alpha=0.5, label = '1Hz')
ax1.hist(coer2pPos_total, bins=bins, alpha=0.5, label = '0.5Hz')
ax1.set_ylabel('Count')
ax1.set_xlabel('Coercive Field')
plt.legend()

fig2, ax2 = plt.subplots(1, 1)
total = coerNeg.size
bin_number = np.ceil(np.sqrt(total))//2*2+1
bins = np.linspace(min(coerNeg),max(coerNeg), num = bin_number)

ax2.hist(coer0pNeg_total, bins=bins, alpha=0.5, label = '0Hz')
ax2.hist(coer1pNeg_total, bins=bins, alpha=0.5, label = '1Hz')
ax2.hist(coer2pNeg_total, bins=bins, alpha=0.5, label = '0.5Hz')

#fit_hist = mlab.normpdf(bins, mu, sigma)
#l = plt.plot(bins, fit_hist, 'r--', linewidth=2)

ax2.set_ylabel('Count')
ax2.set_xlabel('Coercive Field')
plt.legend()
#plt.show()

#########################################################################################################################
'''

def statePD(folder):
	for root, subdirs, files in os.walk(folder):
		for sub in subdirs:
			if 'Square_' in sub:
				path, dirs, fi = next(os.walk(os.path.join(root, sub)))
				file_count = len(fi)
				if file_count > 45:
					savefolder = folder + '\\AnalysedData3\\' + sub
					if not os.path.exists(savefolder):
						os.makedirs(savefolder)
					Lattice.periodDoubleAnalysis(path, savefolder)
					#plt.show()
					#Lattice.folderAnalysis(path, savefolder)
					#plt.show()
					plt.close('all')

for root, subdirs, files in os.walk(folder):
	for sub in subdirs:
		if 'Square_' in sub:
			path, dirs, fi = next(os.walk(os.path.join(root, sub)))
			file_count = len(fi)
			if file_count > 45:
				savefolder = folder + '\\AnalysedData3\\' + sub
				if not os.path.exists(savefolder):
					os.makedirs(savefolder)
				Lattice.periodDoubleAnalysis(path, savefolder)
				#plt.show()
				#Lattice.folderAnalysis(path, savefolder)
				#plt.show()
				plt.close('all')
# import imageio
# images = []
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('/path/to/movie.gif', images)
