import rpmClass_Stable as rpm 		#Most recent version of the RPM artificial spin ice code

from importlib import *			#Package to update the version of rpmClass_Stable
import numpy as np			#Mathematics package

reload(rpm)		#Reloads RPM file

import os
import matplotlib.pyplot as plt

#Material Parameters


Hc = 0.1					#Coercive Field
bar_length = 600e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 20e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)


#Lattice Parameters
size = 20					#Define the size of the lattice


#folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\varyGap'	#The folder for the files to be saved in.
folder = os.getcwd()


lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
field_angle=45.
std_list = np.linspace(0.0, 0.2, 41)
Hmax = 0.1/np.cos(np.pi/4)
Hc = 0.1
Hc_std = 0.
i = 0
lattice.square(Hc, Hc_std)

QD_list = np.linspace(0.0, 0.1, 11)
width_list = np.linspace(50e-9, 500e-9, 10)

for QD in QD_list:
	if i == 1:
		lattice.square(Hc, Hc_std)
	for width in width_list:
		lattice.changeWidth(width)
		for count in np.arange(0, 4):
			lattice.randomMag()
			differentName = 'QD%(QD)e_Width%(width)e_%(count)d' %locals()
			folderloc = os.path.join(folder, differentName)
			lattice.fieldSweep(Hmax, 10, field_angle, n=5, loops=10, folder = folderloc, q1 = True)
	lattice.changeQuenchedDisorder(QD)





#lattice.square()
#loadfolder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\JackLattices\PeriodDoubling\VertexGap4.000000e-08'
#filename = 'InitialRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours4_Loops15.npz'
#lattice.shortShakti(Hc, 0.025)
#lattice.randomMag()
#lattice.save(filename, folder = loadfolder)
#lattice.searchRPM_monte(50, Hmax, steps = 15, n = 4, loops = 20, folder = folder)
#vgap_list = np.linspace(20e-9, 200e-9, 10, endpoint = True) 
#mag_list = np.geomspace(800e3, 800e6, 10, endpoint = True)
#loadfolder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\squarerandomstate3\VertexGap2.000000e-08'
#filename = r'InitialRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours4_Loops15.npz'
lattice.load(os.path.join(loadfolder, filename))
folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\MagStrengthVariation\ShaktiQD2p5'
differentName = 'SatMag%(mag)e' %locals()
folderloc = os.path.join(folder, differentName)
lattice.fieldSweep(Hmax, 10, field_angle, n=4, loops=15, folder = folderloc, q1 = True)


#for mag in mag_list:
	#lattice.square(Hc, Hc_std)
#	lattice.load(os.path.join(loadfolder, filename+'.npz'))
	#lattice.changeMagnetisation(mag)
	#folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\MagStrengthVariation\ShaktiQD2p5'
	#differentName = 'SatMag%(mag)e' %locals()
	#folderloc = os.path.join(folder, differentName)
	#lattice.fieldSweep(Hmax, 10, field_angle, n=4, loops=15, folder = folderloc, q1 = True)

#for Hc_std in std_list:
#	lattice.square(Hc, Hc_std)
#	lattice.randomMag(seed = 1)	
#	lattice.appliedFieldSweep(0.090/np.cos(np.pi/4), 0.11/np.cos(np.pi/4), 11, 10, 45., n=5, loops=5, folder = folder+'\\square7\\Hc_std%(Hc_std)e' %locals())


	#lattice.kagome(Hc, Hc_std)
	#lattice.appliedFieldSweep(0.095, 0.0105, 11, 10, 0./180.*np.pi, n=5, loops=5, folder = folder+r'\kagome')

