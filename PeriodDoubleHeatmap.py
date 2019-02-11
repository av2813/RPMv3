import numpy as np
import os
import matplotlib.pyplot as plt
#import seaborn as sns
import scipy.optimize as sco
from pathlib import Path
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter
import rpmClass_Stable as rpm
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})


#folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\ShaktiPeriodDoubling'
folder = r'D:\RPM_Rapid\SquarePeriodDouble'
savefolder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\PeriodDoublingFigures\ZurichPoster'
name = '3SquareSat_Width500_QD10_'

Lattice = rpm.ASI_RPM(1,1)
QD = []
energy = []
width = []
count = []
perioddouble = []
loops = []
count = []
#countLattice = np.zeros((81,81,9))
data = np.zeros((10, 10, 5))
i=0
for root, subdirs, files in os.walk(folder):
	for file in files:
		if 'FinalRPMLattice' in file and '.npz' in file:
			print(root)
			path, dirs, fi = next(os.walk(root))
			file_count = len(fi)
			filename = os.path.join(root, file)
			try:
				Lattice.load(filename)
			except:
				print('ignore')
			#print(Lattice.returnLattice())
			if i == 0:
				countLattice = Lattice.returnLattice()[:,:,:]
			loops.append(Lattice.returnLattice()[:,:,7].max()/2)
			if file_count > 200:
				#energy.append(Lattice.demagEnergy(5))
				perioddouble.append(Lattice.periodDoubleCounter(10)/Lattice.countSpins()*100)
				print(root[root.find('_QD')+3:root.find('_Width')], root[root.find('_Width')+6:], root)
				countLattice[:,:,7] = np.add(countLattice[:,:,7], Lattice.returnLattice()[:,:,7])
				try:
					QD.append(float(root[root.find('_QD')+3:root.find('_Width')]))
				except:
					print('dont care')
				try:
					width.append(float(root[root.find('_Width')+6:root.find('_Count')]))
				except:
					print('dont care')
				try:
					count.append(int(root[root.find('_Count')+6:]))
				except:
					print('dont care')
				i+=1
			else:
				print(root[root.find('_QD')+3:root.find('_Width')], root[root.find('_Width')+6:], root)
				#energy.append(Lattice.demagEnergy(5))
				perioddouble.append(0)
				try:
					QD.append(float(root[root.find('_QD')+3:root.find('_Width')]))
				except:
					print('dont care')
				try:
					width.append(float(root[root.find('_Width')+6:root.find('_Count')]))
				except:
					print('dont care')
				try:
					count.append(int(root[root.find('_Count')+6:]))
				except:
					print('dont care')
				i+=1

		# #print(sub)
		# print(file)
		# for ro, su, fi in os.walk(os.path.join(root,sub)):
		# 	if len(fi)>4:
		# 		count.append((len(fi)-3)/25)
		# 		#data[i, j, int(ro[-1])] = (len(fi)-3)/25

		# 		#print((count))
		# 		#PeriodDoublingData_QD1.000000e-01_Width1.000000e-07_1
		# 		print(ro[82:94])
		# 		print(ro[100:112])
		# 		try:
		# 			QD.append(float(ro[83:95])*0.1)
		# 		except:
		# 			print('dont care')
		# 		try:
		# 			width.append(float(ro[101:113]))
		# 		except:
		# 			print('dont care')


sumLattice = rpm.ASI_RPM(20, 20, lattice = countLattice)
print(sumLattice.returnLattice())
#sumLattice.graph()




data_dict = {'version':count,'QD':np.array(QD)*100, 'Width':np.array(width)*1e9, 'Count': perioddouble}

data_df = pd.DataFrame(data_dict)
data_group =data_df.groupby(by = ['QD', 'Width']).mean()
print(data_group)
#for name, group in data_group:
#	print(name)
#	print(group.mean())
data = data_df.groupby(['QD', 'Width']).mean()
#new_data = data_df.groupby(['QD']).mean().groupby(['Width']).mean()
#print(data_df)
#print(perioddouble)
#plt.figure()
#plt.scatter(np.array(width)*1000, np.array(QD)*1000, c = np.array(count))
#plt.xlabel('Interaction Strength (mT)')
#plt.ylabel('Quenched disorder')
#plt.colorbar()
sns.set_context('poster', font_scale = 2)
print(data)
piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)
#print(pd.crosstab(data.QD, data.Width))
plt.figure()
print(piv.index.values.round(2))
print(list(piv.index.values.round(2))[::4])
print(piv.index.values.round(2).tolist()[::4])
yticks = piv.index.values.round(2).tolist()[::4]
#yticklabels=piv.index.values.round(2).tolist()[::4]
ax = sns.heatmap(piv, square = True, vmin = 0, vmax =0.5, yticklabels = yticks[::1],cbar_kws={'label': 'Percentage of period doubled spins'}, cmap = 'Blues',  xticklabels=4)
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
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

#plt.scatter(data['Width'], data['QD'], data['Count'])
#plt.show()

plt.savefig(os.path.join(savefolder, name+'Percentage.png'), transparent=True,orientation='portrait')
plt.savefig(os.path.join(savefolder, name+'Percentage.svg'), transparent=True,orientation='portrait')

#print(piv.index.values.round(2))
#print(list(piv.index.values.round(2))[::4])
#print(piv.index.values.round(2).tolist()[::4])

data_dict = {'QD':np.array(QD)*100, 'Width':np.array(width)*1e9, 'Count': loops}
data_df = pd.DataFrame(data_dict)
data = data_df.groupby(['QD', 'Width']).mean()
#new_data = data_df.groupby(['QD']).mean().groupby(['Width']).mean()
print(data_df)
print(perioddouble)
#plt.figure()
#plt.scatter(np.array(width)*1000, np.array(QD)*1000, c = np.array(count))
#plt.xlabel('Interaction Strength (mT)')
#plt.ylabel('Quenched disorder')
#plt.colorbar()
print(data)
piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)
#print(pd.crosstab(data.QD, data.Width))
plt.figure()
sns.set_context('poster', font_scale = 2)
yticks = piv.index.values.round(2).tolist()[::4]
ax = sns.heatmap(piv, square = True, vmin = 0, vmax =10,yticklabels = yticks[::1], cbar_kws={'label': 'Number of loops'}, cmap = 'Blues',  xticklabels=4)
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#ax.set_xticks(xticks*ax.get_xlim()[1]/(2*math.pi))
ax.set_yticks(np.array(yticks)*ax.get_ylim()[1]/10.)
#ax.set_yticks(piv.index.values.round(2).tolist()[::-4])
#ax.set_yticklabels(piv.index.values.round(2).tolist()[::-4])
ax.invert_yaxis()
plt.tight_layout()
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#plt.locator_params(nbins=6)
#ax.yaxis.set_major_locator(plt.MaxNLocator(5))
ax.set_ylabel('Quenched Disorder (%)')
ax.set_xlabel('Width (nm)')
plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
plt.setp(ax.get_yticklabels(), rotation=0, verticalalignment='top')



'''
data_dict = {'QD':np.array(QD)*100, 'Width':np.array(width)*1e9, 'Count': energy}
data_df = pd.DataFrame(data_dict)
data = data_df.groupby(['QD', 'Width']).mean()
#new_data = data_df.groupby(['QD']).mean().groupby(['Width']).mean()
print(data_df)
print(perioddouble)
#plt.figure()
#plt.scatter(np.array(width)*1000, np.array(QD)*1000, c = np.array(count))
#plt.xlabel('Interaction Strength (mT)')
#plt.ylabel('Quenched disorder')
#plt.colorbar()
print(data)
piv = pd.pivot_table(data, values = 'Count', index = ['QD'], columns = ['Width'], fill_value = 0)
#print(pd.crosstab(data.QD, data.Width))
plt.figure()
ax = sns.heatmap(piv, square = True,  cbar_kws={'label': 'Number of loops'}, cmap = 'Blues',  xticklabels=2)
ax.invert_yaxis()
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#plt.locator_params(nbins=6)
#ax.yaxis.set_major_locator(plt.MaxNLocator(5))
ax.set_ylabel('Quenched Disorder (%)')
ax.set_xlabel('Width (nm)')
plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
plt.setp(ax.get_yticklabels(), rotation=0, verticalalignment='top')
'''
#plt.scatter(data['Width'], data['QD'], data['Count'])


#mng = plt.get_current_fig_manager()
#mng.frame.Maximize(True)


plt.savefig(os.path.join(savefolder, name+'Count.png'), transparent=True,orientation='portrait')
plt.savefig(os.path.join(savefolder, name+'Count.svg'), transparent=True,orientation='portrait')
plt.show()


data_dict = {'QD':np.array(QD)*100, 'Width':np.array(width)*1e9, 'Count': loops}