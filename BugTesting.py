import rpmClass_Stable as rpm
import numpy as np
import math
import os
import matplotlib.pyplot as plt
import seaborn as sns
import re
from importlib import *			#Package to update the version of rpmClass_Stable

reload(rpm)
sns.set_style("ticks")
sns.set_palette("colorblind")

def testDumbbellvsDipole():
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

#testDumbbellvsDipole()


def testLattices():
	'''
	To check the creation of all the lattices
	'''
	squareLattice = rpm.ASI_RPM(20,20)
	squareLattice.square()
	squareLattice.graph()
	brickworkLatttice = rpm.ASI_RPM(20,20)
	brickworkLatttice.brickwork()
	brickworkLatttice.graph()
	kagomeLattice = rpm.ASI_RPM(20,20)
	kagomeLattice.kagome()
	kagomeLattice.graph()
	lattice = rpm.ASI_RPM(20,20)
	lattice.squareEdges()
	lattice.graph()
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
	'''
	test all the graphing software
	'''
	lattice= rpm.ASI_RPM(20, 20)
	lattice.square()
	lattice.graph()
	lattice.graphCharge()
	lattice.fieldPlot()
	lattice.vertexTypeMap()
	lattice.magneticOrdering()

def testDemag():
	lattice = rpm.ASI_RPM(21,21)

	lattice.squareEdges(Hc_mean = 0.05, Hc_std = 0.0)
	#lattice.fixEdges()
	lattice.squareGroundState()
	#lattice.fieldPlot()
	#lattice.vertexTypeMap()
	#lattice.graph()
	lattice.randomMag()
	#lattice.changeHc(11, 12, 1.)
	#lattice.flipSpin(11, 12)
	#lattice.changeHc(11, 12, 1.)
	#lattice.flipSpin(33, 34)
	#lattice.changeHc(33, 34, 1.)
	#lattice.flipSpin(15, 16)
	#lattice.changeHc(15, 16, 1.)
	#lattice.flipSpin(27, 34)
	#lattice.changeHc(27, 34, 1.)
	#lattice.flipSpin(19, 34)
	#lattice.changeHc(25, 9, 1.)
	#lattice.flipSpin(25, 9)
	#lattice.vertexTypeMap()
	#lattice.fieldSweep(0.055/np.cos(np.pi/4), 5, 45., n=5, loops = 4, folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\SquareGroundStateSolver\FieldSweep\Square20x20_HappHc_v9', q1 = True)
	#lattice.graph()
	#lattice.vertexTypeMap()
	#lattice.graphCharge()
	#lattice.magneticOrdering()
	lattice.structureFactor(-4*np.pi, 4*np.pi, 60)



testDemag()

def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


#testDemag()
#folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\SquareGroundStateSolver\FieldSweep\Square20x20_HappHc_v9'
#counter = 0
#lattice = rpm.ASI_RPM(20,20)

#lattice.brickwork()
#lattice.save('test3')
#lattice.graph()
#lattice.kagome()
#lattice.load('test3.npz')
#lattice.graph()

# for root, dirs, files in os.walk(folder):
# 	print(files)
# 	files.sort(key = natural_keys)
# 	for file in files:
# 		if 'Lattice_counter' in file:
# 			fileloc = os.path.join(root, file)
# 			lattice.load(fileloc)
# 			print(file, counter)
# 			#lattice.fieldPlot()
# 			lattice.vertexTypeMap()
# 			counter+=1

#testDemag()
#lattice = rpm.ASI_RPM(10,10)
#lattice.square(0.1, 0.01)
#lattice.FORC(0.11, 20, 45., n=4, folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\FORC_testing')
#lattice.FORC2(0.11, 30, 45, n=4, folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\FORC_testing2')
#lattice.kagome()
#lattice.fixEdges()
#lattice.randomMag()
#lattice.square()
#lattice.squareGroundState()
#lattice.squareMonopoleState()
#lattice.squareType3State()
#lattice.graphCharge()
#print(lattice.demagEnergy(5))
#lattice.squareGroundState()
#lattice.squareGroundState()
#lattice.magneticOrdering()
#lattice.structureFactor(-4*np.pi, 4*np.pi, 200)
#lattice.makeMonopole(13, 13, charge = 1, fixed = True)
#lattice.makeMonopole(25,25, charge = -1, fixed = True)
#lattice.graphCharge()
#lattice.demagnetisationProtocol()

#lattice.demagnetisationProtocol2()
#graphingTest()
# x = np.linspace(0, 100, 10000)
# y = (1-x/100.)*np.cos(x*2*np.pi) 
# h0 = y[0::50]
# hc = []
# hu=[]
# for h00 in h0:
# 	for n in np.arange(0, 49, 1):
# 		hu.append((y[n]+h00)/2)
# 		if h00<0:
# 			hc.append(((y[n]-h00)/2))
# 		else:
# 			hc.append(((y[n]-h00)/2))
# plt.plot(hc, hu, '.')
# plt.show()
# plt.plot(x, y)
# plt.plot(x[0::50],h0, 'o')
# plt.show()
