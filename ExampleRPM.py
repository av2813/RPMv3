#Import the necessary packages to run the code
import matplotlib
matplotlib.use('TkAgg')
import rpmClass_Stable as rpm 		#Most recent version of the RPM artificial spin ice code

from importlib import *			#Package to update the version of rpmClass_Stable
import numpy as np			#Mathematics package

reload(rpm)		#Reloads RPM file

import os
import matplotlib.pyplot as plt


#Parameters 

#Material Parameters

Hc = 0.065					#Coercive Field (T)
Hc_std = 5					#Stanard deviation in the coercive field (as a percentage)
bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 13e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 80e3)
#Hc = 0.062					#Coercive Field
#Hc_std = 5					#Stanard deviation in the coercive field (as a percentage)
#bar_length = 600e-9			#Bar length in m
#vertex_gap = 100e-9			#Vertex gap in m
#bar_thickness = 15e-9		#Bar thickness in m
#bar_width = 80e-9			#Bar width in m
#magnetisation = 830e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)


#Lattice Parameters
size = 7					#Define the size of the lattice

#Minor loop Parameters

field_angle = 45.			#Angle at which the field will be applied in degrees
field_max = 0.95*Hc/np.cos(field_angle/180*np.pi)			#Maximum field to by applied at field angle measured in Telsa 

field_max = 1.*Hc/np.cos(np.pi/4)			#Maximum field to by applied at field angle measured in Telsa 
field_angle = 45.			#Angle at which the field will be applied in degrees

steps = 5					#Number of steps between the minimum value of the coercive field
							#and the maxium field specified above. Total number of steps in a 
							#minor loop is = 4*(steps+1)
neighbours = 4				#The radius of neighbouring spins that are included in the local
							#field calculation
loops = 6					#The number of minor field loops to be done

#File information

folder = r'C:\Users\kjs18\Documents\RPM Code\Data\Square_7x7_0%_std'	#The folder for the files to be saved in.


#Define the system
#The parameters defined above go into the function below that defines the 
#characteristics of the lattice.
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice.square(Hc, Hc_std/100)	#Specify whether it is a square or kagome lattice
#lattice.kagome(Hc, Hc_std/100)	#example of kagome

lattice.randomMag()

'''
#Initiate the minor loop (field sweep)
folder = r''
file = r'Lattice_Loop7_FieldStrength-87p68mT_Angle0p79.npz'
for root, dirs, files in os.walk(folder):
	for file in files:
		if file[-4:] == '.npz':
			print(root)
			lattice.load(os.path.join(root, file))
			lattice.latticeFieldHistogram(5, save = False)
			plt.figure()
			plt.title(file)
			lattice.graph()
			plt.show()
'''
#Load and plot
#here = os.path.dirname(os.path.abspath(r'C:/Users/kjs18/Documents/RPM Code/Data/Square_5x5_0%_st/Hmax-1.3517789748205793'))
filename = r"C:\Users\kjs18\Documents\RPM Code\Data\Square_7x7_0%_std\FinalRPMLattice_Hmax9p192388e-02_steps10_Angle7p853982e-01_neighbours3_Loops4.npz"
lattice.load(filename)


#]lattice.searchRPM_single( Hmax = field_max, Htheta = field_angle, steps =10, n=3, loops=4, folder = folder)
#lattice.randomMag()

lattice.magneticOrdering()	
plt.show()

#Initiate the minor loop (field sweep)

#lattice.fieldSweep(Hmax = field_max, steps = steps, \
#					Htheta = field_angle, n=neighbours, \
#					loops=loops, folder = folder)



#lattice.fieldSweepAnalysis(folder)		#produces the RPM graphs 
										#(Correlation, Magnetisation, Monopole density, Vertex percentage)


#Varying the applied field
#field_max = 1.2*Hc/np.cos(field_angle*180/np.pi)
#field_min = Hc*0.8/np.cos(field_angle*180/np.pi)
#field_steps = 20

#lattice.appliedFieldSweep(Hmin = field_min, Hmax = field_max, Hsteps = field_steps, \
#					steps = steps, Htheta = field_angle, n=neighbours, \
#					loops=loops, folder = folder)


#lattice.fieldSweepAnalysis(folder)
#lattice.correlationMatrix(folder)




