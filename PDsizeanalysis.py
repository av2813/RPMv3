import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import rpmClass_Stable as rpm
import os
from matplotlib import rcParams
import pandas as pd

from importlib import *			#Package to update the version of rpmClass_Stable

testfolder = r'D:\RPM_Rapid\SizeDependence\Square_initsat_Size22_n44'
testfile = r'FinalRPMLattice_Hmax1p000000e-01_steps20_Angle7p853982e-01_neighbours5_Loops10.npz'
testfilename= os.path.join(testfolder, testfile)
test = rpm.ASI_RPM(1,1)
test.load(testfilename)
print(test.returnProperties())

folder = r'D:\RPM_Rapid\SizeDependence' 
file = r'PeriodicityAll4.npz'
filename = os.path.join(folder, file)

#lattice = rpm.RPM_ASI()

data = np.load(filename)

lst = data.files
rpminfo = []
for item in lst:
	print(item)
	#print(data[item])
	#print()
	#print(data[item].tolist())
	res = []
	print(data[item])
	if item == 'arr_1':
		for state in data[item]:
			if state == 'sat':
				res.append(1)
			if state == 'ground':
				res.append(0)
			if state == 'rand':
				res.append(2)
			#print(state)
		#elif data[item] == ''
		#rpminfo.append(data[item])
	else:
		for val in data[item]: 
			if val != None : 
				res.append(float(val))
				#print(type(val))
				#print(type(float(val)))
			else:
				res.append(np.nan)


	rpminfo.append(res)

#print(rpminfo)
print(np.shape(np.array(rpminfo)))
rpminfo = np.array(rpminfo).T
rpminfo[np.where(rpminfo == None)] = np.nan
print(np.where(rpminfo == None))
rpminfo_df = pd.DataFrame(rpminfo, columns = ['a','b', 'c','d'])

print(rpminfo_df)

rpminfo_df = rpminfo_df.drop(['d'], axis = 1)
print(rpminfo_df)
newdf = rpminfo_df.astype(float)
data = newdf.groupby(by=['c', 'b'])#
data_ground = []
data_sat = []
data_rand = []
for name, group in data:
	print(name, group)
	size, state = name
	period_mean = group['a'].mean()
	period_std = group['a'].std()

	plt.figure()
	plt.hist(group['a'].dropna())
	plt.title('Size: '+str(size)+', State: '+str(state))
	plt.show()
	if state == 0:
		data_ground.append([size, period_mean, period_std])
	if state == 1:
		data_sat.append([size, period_mean, period_std])
	if state == 2:
		data_rand.append([size, period_mean, period_std])
data_ground = np.array(data_ground)
data_sat = np.array(data_sat)
data_rand = np.array(data_rand)
print(data_ground,data_sat,data_rand)

plt.figure()
plt.errorbar(data_ground[:, 0], data_ground[:,1],marker = 'o', yerr = data_ground[:,2], label = 'Ground')
plt.errorbar(data_sat[:, 0], data_sat[:,1],marker = 'o', yerr = data_sat[:,2], label = 'Saturated')
plt.errorbar(data_rand[:, 0], data_rand[:,1],marker = 'o', yerr = data_rand[:,2], label = 'Random')
plt.legend()
plt.ylabel('Average period to reach RPM (number of minor loops)')
plt.xlabel('Size of the array')
#plt.show()

plt.figure()
plt.hist(data_ground[:,1])
plt.show()


	#print(group['a'].std(), group['a'].mean())


testdata = rpminfo[np.where()]
print(data)
print(data.mean())
print(data.std())
newdata = data.mean(numeric_only =True) 
datastd = newdf.groupby(by=['c', 'b']).Groupby.std(numeric_only =True)
print(newdata.values)
groundstate = []
satstate = []
randstate = []
groundstate_err = []
satstate_err = []
randstate_err = []
for x,err, count in zip(newdata.values[:,0],datastd.values[:,0], np.arange(0,27)):
	print(count, x)
	if count%3 == 0:
		groundstate.append(x)
		groundstate_err.append(xerr)
	if (count-1)%3 == 0:
		satstate.append(x)
		satstate_err.append(xerr)
	if (count-2)%3 == 0:
		randstate.append(x)
		randstate_err.append(xerr)
print(groundstate, satstate, randstate)
sizedata = np.reshape(newdata.values[:, 0], [3,9])
#print(newdata['c'].values)
print(sizedata)
sizes = [5,10,12, 15, 18, 20, 22, 25, 30]
plt.figure()
plt.errorbar(sizes, groundstate,yerr = groundstate_err, label = 'Ground')
plt.errorbar(sizes, satstate, yerr = satstate_err, label = 'Saturated')
plt.errorbar(sizes, randstate, yerr = randstate_err, label = 'Random')
plt.legend()
plt.ylabel('Average period to reach RPM (number of minor loops)')
plt.xlabel('Size of the array')
plt.show()
for label, y in zip(['Ground', 'Saturated', 'Random'],sizedata):
	print(y)
	plt.plot([5,10,12, 15, 18, 20, 22, 25, 30], y, '.-', label = label)
#plt.plot([5,10,12, 15, 18, 20, 22, 25, 30], newdata.values[:, 0], 'o')
plt.ylabel('Average period to reach RPM (number of minor loops)')
plt.xlabel('Size of the array')
plt.legend()
plt.show()




