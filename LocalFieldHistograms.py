import rpmClass_Stable as rpm
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)
sns.set_style("ticks")
sns.set_palette("deep")

def localFieldHistogram(lattice, x, y, n, total):
	for test in np.arange(1, n):
		print(n)
		lattice.changeinteractionType('dipole')
		fields = lattice.localFieldHistogram(x, y, test, total, save = True)
		lattice.changeinteractionType('dumbbell')
		fields = lattice.localFieldHistogram(x, y, test, total, save = True)

def latticeFieldHistogram(lattice, n):
	for test in np.arange(1, n):
		print(test)
		lattice.changeinteractionType('dipole')
		fields = lattice.latticeFieldHistogram(test, save = True)
		lattice.changeinteractionType('dumbbell')
		fields = lattice.latticeFieldHistogram(test, save = True)
'''
folder = os.getcwd()
number = 75

Lattice = rpm.ASI_RPM(number,number,bar_length = bar_length, vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        bar_width = bar_width, magnetisation = magnetisation)

parameters = np.array([bar_length, vertex_gap, bar_thickness, bar_width, magnetisation])

Lattice.square(Hc_mean = Hc, Hc_std=Hc_std)
width_list = np.linspace(40e-9, 200e-9, 75)
mu_list=[]
sigma_list = []
field_list = []
print('width')
for wid in width_list:
	print(wid)
	Lattice.changeWidth(wid)
	Lattice.square(Hc_mean = Hc, Hc_std=Hc_std)
	Lattice.randomMag()
	field = Lattice.latticeFieldHistogram(5, save = True)
	mu_list.append(np.mean(field))
	sigma_list.append(np.std2(field))
	field_list.append(field)
sigma_list = np.array(sigma_list)
mu_list = np.array(mu_list)
width_list = np.array(width_list)
field_list = np.array(field_list)
figurename = os.path.join(folder, 'HistogramWidth')
plt.figure()
plt.plot(width_list*1e-9, mu_list*1e-3, '-o')
plt.ylabel('Local field average (mT)')
plt.xlabel('width (nm)')
plt.savefig(figurename+'Average.png')

plt.figure()
plt.plot(width_list*1e-9, sigma_list*1e-3, '-o')
plt.ylabel('Local field standard deviation (mT)')
plt.xlabel('Width (nm)')
plt.savefig(figurename+'Std.png')
'''
#Define the parameters for the lattice
Hc = 0.062					#Coercive Field
Hc_std = 5					#Stanard deviation in the coercive field (as a percentage)
bar_length = 600e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 15e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 830e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters
size = 100					#Define the size of the lattice


lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)

number = 10000
neighbourRadius = 10

#lattice.kagome(Hc, Hc_std/100)
#lattice.randomMag()
#lattice.localPlot(31, 60, 0)
#latticeFieldHistogram(lattice, neighbourRadius)
#lattice.square(Hc, Hc_std/100)
#lattice.randomMag()
#latticeFieldHistogram(lattice, neighbourRadius)
#lattice.localPlot(31,30, 0)
#lattice.shortShakti(Hc, Hc_std/100)
#lattice.randomMag()
#latticeFieldHistogram(lattice, neighbourRadius)
#lattice.localPlot(60, 61, 0)
#lattice.tetris(Hc, Hc_std/100)
#lattice.randomMag()
#latticeFieldHistogram(lattice, neighbourRadius)
#lattice.localPlot(241, 240, 0)

'''
name = 'short_shakti'
folder = r'C:\Users\av2813\Documents\GitHub\RPMv3\\'+name+r'dumbbell_localFieldLatticeHistogram_length6.00E-07width8.00E-08vgap1.00E-07thick1.50E-08'
file= 'Histogram_n8.csv'
filename = os.path.join(folder, file)
dumbbell = np.loadtxt(filename, delimiter =',')
folder = r'C:\Users\av2813\Documents\GitHub\RPMv3\\'+name+r'dipole_localFieldLatticeHistogram_length6.00E-07width8.00E-08vgap1.00E-07thick1.50E-08'
file= 'Histogram_n8.csv'
filename = os.path.join(folder, file)
dipole = np.loadtxt(filename, delimiter =',')

Hc= np.random.normal(loc=50, scale=0.05*60, size=len(dumbbell))
plt.figure()

plt.title(name+' local field distribution')
sns.distplot(dumbbell*1000, hist = True,bins =None,norm_hist = False, kde = True,kde_kws={'kernel':'epa'}, label = 'Dumbbell model')
sns.distplot(dipole*1000, hist = True,bins = None,norm_hist = False, kde = True,kde_kws={'kernel':'epa'}, label = 'Dipole model')
#sns.kdeplot(dumbbell*1000, data2 = Hc, shade = True, cbar =True)
plt.xlabel('Magnetic Field (mT)')
plt.ylabel('\"Density\"')
plt.legend()
folder = os.getcwd()
file = name+'Dist_comparison'
filename = os.path.join(folder, file)
#plt.savefig(filename+'.png')
#plt.savefig(filename+'.svg')
plt.show()
'''