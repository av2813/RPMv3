import rpmClass_Stable as rpm
import os
from importlib import *
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import time
import pandas as pd


reload(rpm)		#make sure that the class is updated with any changes

#parameters
Hc = 0.062
Hc_std = 0.05
bar_length = 400e-9
vertex_gap = 100e-9
bar_thickness = 15e-9
bar_width = 80e-9
magnetisation = 800e3


folder = os.path.join(r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\DumbbellHistogram_Multiparametersweep', 'kagome')
if not os.path.exists(folder):
    os.makedirs(folder)

number = 75

Lattice = rpm.ASI_RPM(number,number,bar_length = bar_length, vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        bar_width = bar_width, magnetisation = magnetisation)

parameters = np.array([bar_thickness,  magnetisation])

Lattice.kagome(Hc_mean = Hc, Hc_std=Hc_std)
length_len = 20
width_len = 10
gap_len = 10
width_list = np.linspace(40e-9, 200e-9, width_len)
length_list = length_list = np.linspace(160e-9, 1000e-9, length_len)
gap_list = np.linspace(15e-9, 150e-9, gap_len)
gap_list = np.append(gap_list, np.linspace(151e-9, 1000e-9, gap_len))
mu_list=[]
sigma_list = []
field_list = []
l_list = []
w_list = []
g_list = []
print('width')
i,j,k = 0,0,0
data = np.zeros((length_len+1, width_len+1, 2*gap_len+1, 5))
for length in length_list:
	Lattice.changeLength(length)
	j = 0
	for width in width_list:
		Lattice.changeWidth(width)
		k = 0
		for gap in gap_list:
			Lattice.changeVertexgap(gap)
			Lattice.kagome(Hc_mean = Hc, Hc_std=Hc_std)
			Lattice.randomMag()
			(mu, sigma, field) = Lattice.latticeFieldHistogram(5, save = True, folder = folder)
			mu_list.append(mu)
			sigma_list.append(sigma)
			field_list.append(field)
			l_list.append(length)
			g_list.append(gap)
			w_list.append(width)
			data[i,j,k,:] = np.array([length, width, gap, mu, sigma])
			print(data[i,j,k,:])
			k+=1
		j+=1
	i+=1
data_dict = {'length':l_list, 'gap':g_list, 'width':w_list, 'mu':mu_list, 'sigma':sigma_list}
data_df = pd.DataFrame(data_dict) 
data_df.to_csv(os.path.join(folder, r'HistogramMultiparameterData.txt'), sep=' ', mode='a')
sigma_list = np.array(sigma_list)
mu_list = np.array(mu_list)
width_list = np.array(width_list)
gap_list = np.array(gap_list)
length_list = np.array(length_list)
field_list = np.array(field_list)
figurename = os.path.join(folder, 'HistogramMultiparameter')
#plt.figure()
#plt.plot(width_list/1e-9, sigma_list/1e-3, '-o')
#plt.ylabel('Local field average (mT)')
#plt.xlabel('width (nm)')
#plt.savefig(figurename+'Average.png')
#plt.savefig(figurename+'Average.svg')

#plt.figure()
#plt.plot(width_list/1e-9, sigma_list/1e-3, '-o')
#plt.ylabel('Local field standard deviation (mT)')
#plt.xlabel('Width (nm)')
#plt.savefig(figurename+'Std.png')
#plt.savefig(figurename+'Std.svg')

filename =  os.path.join(folder, 'HistogramMultiparameterData')
np.savez(filename,parameters,length_list, width_list, sigma_list, mu_list, field_list)