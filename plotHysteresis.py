import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import rpmClass_Stable as rpm
import os
from matplotlib import rcParams
import pandas as pd



sns.set_context('poster', font_scale =2)
sns.set_style('ticks')
sns.set_palette('cubehelix', 7)
rcParams.update({'figure.autolayout': True})

Lattice = rpm.ASI_RPM(1,1)

#fieldStr = []
#field = []
#mag = []
#monopole = []
data = []


def sortFunc(element, begin_str = 'counter', end_str = '_Loop', integer = True):
    #print(element)
    begin = element.find(begin_str)+len(begin_str)
    end = element.find(end_str)
    if end_str =='':
    	end = len(element)
    if integer == True:
    	return(int(element[begin:end]))
    else:
    	return(element[begin:end])

def plotHysteresis(folders=[]):
	data = []
	for folder in folders:
		fieldStr = [0]
		field = [np.array([0,0])]
		mag = [1]
		monopole = [0]
		for root, subpath, files in os.walk(folder):
			new_files = list(filter(lambda x: 'Lattice_counter' in x, files))
			new_files.sort(key = sortFunc)
			for file in new_files:
				if 'Lattice_counter' in file:
					Lattice.load(os.path.join(root, file))
					#print(file[file.find('_Angle')+6:file.find('.npz')])
					angle = float(file[file.find('_Angle')+6:file.find('.npz')].replace('p', '.'))
					Happlied = float(file[file.find('Applied')+7:file.find('_Angle')].replace('p', '.'))
					fieldStr.append(Happlied)
					field.append(np.array([Happlied*np.cos(angle), Happlied*np.sin(angle)]))
					magnew = Lattice.netMagnetisation()
					mag.append(magnew[0]+magnew[1])
					monopole.append(Lattice.monopoleDensity())
					if sortFunc(file) == 202:
						Happlied = 0
						fieldStr.append(Happlied)
						field.append(np.array([Happlied*np.cos(angle), Happlied*np.sin(angle)]))
						magnew = Lattice.netMagnetisation()
						mag.append(magnew[0]+magnew[1])
						monopole.append(Lattice.monopoleDensity())
		fieldStr.append(0)
		field.append(np.array([0, 0]))
		mag.append(1)
		monopole.append(0)
		print(root)
		n = sortFunc(root, '_n', '')
		steps = sortFunc(root, 'Steps', '_n')
		QD = float(sortFunc(root, '_QD', '_Steps', False))
		print(n, steps, QD)
		data.append([fieldStr, field, mag, monopole, steps, n, QD])
		#fig, ax = plt.subplots(2,1)
		#ax[0].plot(data[-1][0], data[-1][2], '.-')
		#ax[1].plot(data[-1][0], data[-1][3], '.-')
		#plt.show()
	return(data)

i=0
folder = r'D:\RPM_Rapid\SquareCheckHysteresis'
sub_list = []
for root, subpaths, files in os.walk(folder):

	for sub in subpaths:
		try:
			sub_list.append(os.path.join(root, sub))
		except:
			print('dont care')

print(sub_list)
if os.path.exists(os.path.join(folder, 'AnalysisData.npz')):
	npzfile = np.load(os.path.join(folder, 'AnalysisData.npz'))
	data_hysteresis = npzfile['arr_0']
else:
	data_hysteresis = plotHysteresis(sub_list)
	data_hy = np.array(data_hysteresis)
	np.savez_compressed(os.path.join(folder, 'AnalysisData'),data_hy)

for data in data_hysteresis:
	print(data)
	fig_list = []
	QD = data[6]
	if QD == 0.1:
		plt.figure(data[4]+100)
		plt.title('Hysteresis Loop QD10% - '+str(data[5])+'n')
		plt.subplot(211)
		plt.plot(data[0], data[2], '.-', label = str(data[4]))
		plt.subplot(212)
		plt.plot(data[0], data[3], '.-')
		plt.legend()
	if QD == 0.05:
		plt.figure(data[4]+200)
		plt.title('Hysteresis Loop QD5% - '+str(data[5])+'n')
		plt.subplot(211)
		plt.plot(data[0], data[2], '.-',label = str(data[4]))
		plt.subplot(212)
		plt.plot(data[0], data[3], '.-')
		plt.legend()
	if QD == 0.01:
		plt.figure(data[4]+300)
		plt.title('Hysteresis Loop QD1% - '+str(data[5])+'n')
		plt.subplot(211)
		plt.plot(data[0], data[2], '.-',label = str(data[4]))
		plt.subplot(212)
		plt.plot(data[0], data[3], '.-')
		plt.legend()
plt.show()
savefolder = r'D:\RPM_Rapid\Hysteresis\HysteresisFigures'
name = 'HysteresisPlot2'

#folder1 = r'D:\RPM_Rapid\Hysteresis\BrickworkHysteresisData_QD1.000000e-01'
#folder2 = r'D:\RPM_Rapid\Hysteresis\BrickworkHysteresisData_QD5.000000e-02'
#folder3 = r'D:\RPM_Rapid\Hysteresis\BrickworkHysteresisData_QD1.000000e-02'

folders_Brickwork = [folder1, folder2, folder3]
data_Brickwork = plotHysteresis(folders_Brickwork)
fig, axes = plt.subplots(2,1, sharex=True)
axes[0].plot(np.array(data_Brickwork[0][0])*np.cos(np.pi/4), data_Brickwork[0][2], '-', label = '10%')
axes[0].plot(np.array(data_Brickwork[1][0])*np.cos(np.pi/4), data_Brickwork[1][2], '-', label = '5%')
axes[0].plot(np.array(data_Brickwork[2][0])*np.cos(np.pi/4), data_Brickwork[2][2], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[0].set_ylabel('Magnetisation')
plt.legend()

axes[1].plot(np.array(data_Brickwork[0][0])*np.cos(np.pi/4), data_Brickwork[0][3], '-', label = '10%')
axes[1].plot(np.array(data_Brickwork[1][0])*np.cos(np.pi/4), data_Brickwork[1][3], '-', label = '5%')
axes[1].plot(np.array(data_Brickwork[2][0])*np.cos(np.pi/4), data_Brickwork[2][3], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[1].set_ylabel('Defect density')
plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(savefolder, name+'Brickworkv3.png'), transparent=True)
plt.savefig(os.path.join(savefolder, name+'Brickworkv3.svg'), transparent=True)



plt.show()



