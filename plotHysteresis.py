import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import rpmClass_Stable as rpm
import os
from matplotlib import rcParams



sns.set_context('poster', font_scale =2)
sns.set_style('ticks')
rcParams.update({'figure.autolayout': True})

Lattice = rpm.ASI_RPM(1,1)

#fieldStr = []
#field = []
#mag = []
#monopole = []
data = []


def sortFunc(element):
    #print(element)
    begin = element.find('counter')+7
    end = element.find('_Loop')
    #print(element.find('counter'))
    #print(element.find('_Loop'))
    #print((element[begin:end]))
    return(int(element[begin:end]))


def plotHysteresis(folders=[]):
	data = []
	for folder in folders:
		fieldStr = []
		field = []
		mag = []
		monopole = []
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
		data.append([fieldStr, field, mag, monopole])
	return(data)


savefolder = r'D:\RPM_Rapid\Hysteresis\HysteresisFigures'
name = 'HysteresisPlot2'

folder1 = r'D:\RPM_Rapid\Hysteresis\BrickworkHysteresisData_QD1.000000e-01'
folder2 = r'D:\RPM_Rapid\Hysteresis\BrickworkHysteresisData_QD5.000000e-02'
folder3 = r'D:\RPM_Rapid\Hysteresis\BrickworkHysteresisData_QD1.000000e-02'

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


folder1 = r'D:\RPM_Rapid\Hysteresis\SquareHysteresisData_QD1.000000e-01'
folder2 = r'D:\RPM_Rapid\Hysteresis\SquareHysteresisData_QD5.000000e-02'
folder3 = r'D:\RPM_Rapid\Hysteresis\SquareHysteresisData_QD1.000000e-02'

folders_Square = [folder1, folder2, folder3]
data_Square = plotHysteresis(folders_Square)

fig, axes = plt.subplots(2,1, sharex=True)
axes[0].plot(np.array(data_Square[0][0])*np.cos(np.pi/4), data_Square[0][2], '-', label = '10%')
axes[0].plot(np.array(data_Square[1][0])*np.cos(np.pi/4), data_Square[1][2], '-', label = '5%')
axes[0].plot(np.array(data_Square[2][0])*np.cos(np.pi/4), data_Square[2][2], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[0].set_ylabel('Magnetisation')
plt.legend()

axes[1].plot(np.array(data_Square[0][0])*np.cos(np.pi/4), data_Square[0][3], '-', label = '10%')
axes[1].plot(np.array(data_Square[1][0])*np.cos(np.pi/4), data_Square[1][3], '-', label = '5%')
axes[1].plot(np.array(data_Square[2][0])*np.cos(np.pi/4), data_Square[2][3], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[1].set_ylabel('Defect density')
plt.legend()
plt.tight_layout()


plt.savefig(os.path.join(savefolder, name+'Squarev3.png'), transparent=True)
plt.savefig(os.path.join(savefolder, name+'Squarev3.svg'), transparent=True)


folder1 = r'D:\RPM_Rapid\Hysteresis\ShaktiHysteresisData_QD1.000000e-01'
folder2 = r'D:\RPM_Rapid\Hysteresis\ShaktiHysteresisData_QD5.000000e-02'
folder3 = r'D:\RPM_Rapid\Hysteresis\ShaktiHysteresisData_QD1.000000e-02'

folders_Shakti = [folder1, folder2, folder3]
data_Shakti = plotHysteresis(folders_Shakti)

fig, axes = plt.subplots(2,1, sharex=True)
axes[0].plot(np.array(data_Shakti[0][0])*np.cos(np.pi/4), data_Shakti[0][2], '-', label = '10%')
axes[0].plot(np.array(data_Shakti[1][0])*np.cos(np.pi/4), data_Shakti[1][2], '-', label = '5%')
axes[0].plot(np.array(data_Shakti[2][0])*np.cos(np.pi/4), data_Shakti[2][2], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[0].set_ylabel('Magnetisation')
plt.legend()

axes[1].plot(np.array(data_Shakti[0][0])*np.cos(np.pi/4), data_Shakti[0][3], '-', label = '10%')
axes[1].plot(np.array(data_Shakti[1][0])*np.cos(np.pi/4), data_Shakti[1][3], '-', label = '5%')
axes[1].plot(np.array(data_Shakti[2][0])*np.cos(np.pi/4), data_Shakti[2][3], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[1].set_ylabel('Defect density')
plt.legend()
plt.tight_layout()


plt.savefig(os.path.join(savefolder, name+'Shaktiv3.png'), transparent=True)
plt.savefig(os.path.join(savefolder, name+'Shaktiv3.svg'), transparent=True)



folder1 = r'D:\RPM_Rapid\Hysteresis\TetrisHysteresisData_QD1.000000e-01'
folder2 = r'D:\RPM_Rapid\Hysteresis\TetrisHysteresisData_QD5.000000e-02'
folder3 = r'D:\RPM_Rapid\Hysteresis\TetrisHysteresisData_QD1.000000e-02'

folders_Tetris = [folder1, folder2, folder3]
data_Tetris = plotHysteresis(folders_Tetris)

fig, axes = plt.subplots(2,1, sharex=True)
axes[0].plot(np.array(data_Tetris[0][0])*np.cos(np.pi/4), data_Tetris[0][2], '-', label = '10%')
axes[0].plot(np.array(data_Tetris[1][0])*np.cos(np.pi/4), data_Tetris[1][2], '-', label = '5%')
axes[0].plot(np.array(data_Tetris[2][0])*np.cos(np.pi/4), data_Tetris[2][2], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[0].set_ylabel('Magnetisation')
plt.legend()

axes[1].plot(np.array(data_Tetris[0][0])*np.cos(np.pi/4), data_Tetris[0][3], '-', label = '10%')
axes[1].plot(np.array(data_Tetris[1][0])*np.cos(np.pi/4), data_Tetris[1][3], '-', label = '5%')
axes[1].plot(np.array(data_Tetris[2][0])*np.cos(np.pi/4), data_Tetris[2][3], '-', label = '1%')
plt.xticks(np.array([-0.1, 0, 0.1]), (r'-$H_{c}$', 0, r'$H_{c}$'))
plt.xlabel('Applied Field')
axes[1].set_ylabel('Defect density')
plt.legend()
plt.tight_layout()


plt.savefig(os.path.join(savefolder, name+'Tetrisv3.png'), transparent=True)
plt.savefig(os.path.join(savefolder, name+'Tetrisv3.svg'), transparent=True)

plt.show()



