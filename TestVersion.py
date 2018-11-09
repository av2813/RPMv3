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
size = 25					#Define the size of the lattice


folder = r'C:\Users\av2813\Box\GitHub\RPM\RPM_Data\QuenchedDisorder_variation'	#The folder for the files to be saved in.



lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
field_angle=45.
std_list = np.linspace(0.0, 0.2, 11)
for Hc_std in std_list:
	lattice.square(Hc, Hc_std)
	lattice.randomMag(seed = 1)	
	lattice.appliedFieldSweep(0.090/np.cos(np.pi/4), 0.011/np.cos(np.pi/4), 11, 10, 45., n=5, loops=5, folder = folder+'\\square6\\Hc_std%(Hc_std)e' %locals())


	#lattice.kagome(Hc, Hc_std)
	#lattice.appliedFieldSweep(0.095, 0.0105, 11, 10, 0./180.*np.pi, n=5, loops=5, folder = folder+r'\kagome')

