import rpmClass_Stable as rpm
import os
from importlib import *
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
import time

reload(rpm)		#make sure that the class is updated with any changes

#parameters
Hc = 0.062
Hc_std = 0.05
bar_length = 400e-9
vertex_gap = 100e-9
bar_thickness = 15e-9
bar_width = 80e-9
magnetisation = 800e3

folder = os.path.join(r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\DumbbellHistogram_parametersweep', 'shortShakti')
if not os.path.exists(folder):
    os.makedirs(folder)
number = 75

Lattice = rpm.ASI_RPM(number,number,bar_length = bar_length, vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        bar_width = bar_width, magnetisation = magnetisation)

parameters = np.array([bar_length, vertex_gap, bar_thickness, bar_width, magnetisation])

Lattice.shortShakti(Hc_mean = Hc, Hc_std=Hc_std)
width_list = np.linspace(40e-9, 200e-9, 75)
mu_list=[]
sigma_list = []
field_list = []
print('width')
for wid in width_list:
	print(wid)
	Lattice.changeWidth(wid)
	Lattice.shortShakti(Hc_mean = Hc, Hc_std=Hc_std)
	Lattice.randomMag()
	(mu, sigma, field) = Lattice.latticeFieldHistogram(5, save = True)
	mu_list.append(mu)
	sigma_list.append(sigma)
	field_list.append(field)
sigma_list = np.array(sigma_list)
mu_list = np.array(mu_list)
width_list = np.array(width_list)
field_list = np.array(field_list)
figurename = os.path.join(folder, 'HistogramWidth')
plt.figure()
plt.plot(width_list/1e-9, mu_list/1e-3, '-o')
plt.ylabel('Local field average (mT)')
plt.xlabel('width (nm)')
plt.savefig(figurename+'Average.png')
plt.savefig(figurename+'Average.svg')

plt.figure()
plt.plot(width_list/1e-9, sigma_list/1e-3, '-o')
plt.ylabel('Local field standard deviation (mT)')
plt.xlabel('Width (nm)')
plt.savefig(figurename+'Std.png')
plt.savefig(figurename+'Std.svg')

filename =  os.path.join(folder, 'HistogramWidthData')
np.savez(filename,parameters, width_list, sigma_list, mu_list, field_list)

Lattice = rpm.ASI_RPM(number,number,bar_length = bar_length, vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        bar_width = bar_width, magnetisation = magnetisation)

Lattice.shortShakti(Hc_mean = Hc, Hc_std=Hc_std)
length_list = np.linspace(160e-9, 1000e-9, 100)
mu_list=[]
sigma_list = []
field_list = []
print('length')
for wid in length_list:
	print(wid)
	Lattice.changeLength(wid)
	Lattice.shortShakti(Hc_mean = Hc, Hc_std=Hc_std)
	Lattice.randomMag()
	(mu, sigma, field) = Lattice.latticeFieldHistogram(5, save = True)
	mu_list.append(mu)
	sigma_list.append(sigma)
	field_list.append(field)
sigma_list = np.array(sigma_list)
mu_list = np.array(mu_list)
field_list = np.array(field_list)
figurename = os.path.join(folder, 'HistogramLength')
plt.figure()
plt.plot(length_list/1e-9, mu_list/1e-3, '-o')
plt.ylabel('Local field average (mT)')
plt.xlabel('Length (nm)')
plt.savefig(figurename+'Average.png')
plt.savefig(figurename+'Average.svg')

plt.figure()
plt.plot(length_list/1e-9, sigma_list/1e-3, '-o')
plt.ylabel('Local field standard deviation (mT)')
plt.xlabel('Length (nm)')
plt.savefig(figurename+'Std.png')
plt.savefig(figurename+'Std.svg')

filename =  os.path.join(folder, 'HistogramLengthData')
np.savez(filename,parameters, length_list, sigma_list, mu_list, field_list)

Lattice = rpm.ASI_RPM(number,number,bar_length = bar_length, vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        bar_width = bar_width, magnetisation = magnetisation)

Lattice.shortShakti(Hc_mean = Hc, Hc_std=Hc_std)
gap_list = np.linspace(15e-9, 150e-9, 80)
gap_list = np.append(gap_list, np.linspace(151e-9, 1000e-9, 40))
mu_list=[]
sigma_list = []
field_list = []
print('gap')
for wid in gap_list:
	print(wid)
	Lattice.changeVertexgap(wid)
	Lattice.shortShakti(Hc_mean = Hc, Hc_std=Hc_std)
	Lattice.randomMag()
	(mu, sigma, field) = Lattice.latticeFieldHistogram(5, save = True)
	mu_list.append(mu)
	sigma_list.append(sigma)
	field_list.append(field)
sigma_list = np.array(sigma_list)
mu_list = np.array(mu_list)
field_list = np.array(field_list)
figurename = os.path.join(folder, 'HistogramGap')
plt.figure()
plt.plot(gap_list/1e-9, mu_list/1e-3, '-o')
plt.ylabel('Local field average (mT)')
plt.xlabel('Vertex gap (nm)')
plt.savefig(figurename+'Average.png')
plt.savefig(figurename+'Average.svg')

plt.figure()
plt.plot(gap_list/1e-9, sigma_list/1e-3, '-o')
plt.ylabel('Local field standard deviation (mT)')
plt.xlabel('Vertex gap (nm)')
plt.savefig(figurename+'Std.png')
plt.savefig(figurename+'Std.svg')

filename =  os.path.join(folder, 'HistogramGapData')
np.savez(filename,parameters, gap_list, sigma_list, mu_list, field_list)

