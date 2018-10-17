import rpmClass_Stable as rpm
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)
sns.set_style("ticks")
sns.set_palette("colorblind")

def testDumbellvsDipole():
	'''
	To test the difference between the dumbbell and the dipole model
	'''
	lattice= rpm.ASI_RPM(50, 50)
	test = lattice.dumbbell([1.,0.], [40e-9,100e-9], [0., 500e-9])*1000
	test2 = lattice.dipole([1.,0.], [40e-9,100e-9], [0., 500e-9])*1000
	print('Dumbbell magnetic field', test)
	print('Dipole interaction model magnetic field', test2, 'mT')
	print('Difference between dumbbell and dipole model', test-test2, 'mT')
	print('Percentage difference', (np.linalg.norm(test)-np.linalg.norm(test2))/np.linalg.norm(test2),'%')

	dist_list =np.linspace(1e-9, 10e-6, 1000)
	per_diff =np.zeros((dist_list.size, dist_list.size))
	i, j =0, 0
	for x in dist_list:
		j=0
		for y in dist_list:
			dip = lattice.dipole([1, 0], [x, y], [0,0])
			dumb = lattice.dumbbell([1, 0], [x, y], [0,0])
			per_diff[i, j]=((np.linalg.norm(dip)-np.linalg.norm(dumb))/np.linalg.norm(dip))
			j+=1
		i+=1

	fig, ax = plt.subplots()
	im = ax.imshow(np.log10(per_diff), origin = 'lower', cmap = 'inferno')
	cbar = ax.figure.colorbar(im, ax=ax)
	strings = ["%.0f" % number for number in np.linspace(1e-9, 10e-6, 11)*1e9]
	ax.set_xticks(np.linspace(0, dist_list.size, 11))
	ax.set_xticklabels(strings)
	ax.set_yticks(np.linspace(0, dist_list.size, 11))
	ax.set_yticklabels(strings)
	ax.set_xlabel('Distance in x direction (nm)')
	ax.set_ylabel('Distance in y direction (nm)')

	dist_list =np.linspace(10e-9, 10e-6, 10000)
	per_diff =np.zeros((dist_list.size))
	i, j =0, 0
	const_y = 500e-9
	for x in dist_list:
		dip = lattice.dipole([1, 0], [x, const_y], [0,0])
		dumb = lattice.dumbbell([1, 0], [x, const_y], [0,0])
		per_diff[i]=((np.linalg.norm(dip)-np.linalg.norm(dumb))/np.linalg.norm(dip))
		i+=1
	fig, ax = plt.subplots()
	ax.plot(dist_list, per_diff, '-')
	ax.set_xlabel('Distance in x direction (nm)')
	ax.set_ylabel('Percentage Difference between Dipole and Dumbbell interaction')
	ax.set_title(r'Difference between field: y-offset %.0fnm' %(const_y*1e9))
	plt.show()
	plt.show()


def testLattices():
	squareLattice = rpm.ASI_RPM(20,20)
	squareLattice.square()
	squareLattice.graph()
	kagomeLattice = rpm.ASI_RPM(20,20)
	kagomeLattice.kagome()
	kagomeLattice.graph()
	tetrisLattice = rpm.ASI_RPM(10,10)
	tetrisLattice.tetris()
	tetrisLattice.graph()
	shaktiLattice = rpm.ASI_RPM(20,20)
	shaktiLattice.shortShakti()
	shaktiLattice.graph()
	shaktiLattice = rpm.ASI_RPM(20,20)
	shaktiLattice.longShakti()
	shaktiLattice.graph()


#testLattices()



def graphingTest():
	lattice= rpm.ASI_RPM(20, 20)
	lattice.square()
	lattice.graph()
	lattice.graphCharge()
	lattice.fieldPlot()
	lattice.vertexTypeMap()
	lattice.magneticOrdering()

graphingTest()
plt.show()
