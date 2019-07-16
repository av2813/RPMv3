#Import the necessary packages to run the code
import matplotlib

import rpmClass_Stable as rpm 		#Most recent version of the RPM artificial spin ice code
from importlib import *			#Package to update the version of rpmClass_Stable
import numpy as np			#Mathematics package

reload(rpm)		#Reloads RPM file

import os
import matplotlib.pyplot as plt


#Parameters 

#Material Parameters

Hc = 0.062					#Coercive Field (T)
Hc_std = 0.00001					#Stanard deviation in the coercive field (as a percentage)
bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 14e-9		#Bar thickness in m
bar_width = 190e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 80e3)



#Lattice Parameters
size = 11					#Define the size of the lattice

#Minor loop Parameters

field_angle = 45.			#Angle at which the field will be applied in degrees
field_max = Hc			#Maximum field to by applied at field angle measured in Telsa 

field_max2 = 1*Hc/np.cos(field_angle/180*np.pi)			#Maximum field to by applied at field angle measured in Telsa 
			#Angle at which the field will be applied in degrees

steps = 20					#Number of steps between the minimum value of the coercive field
							#and the maxium field specified above. Total number of steps in a 
							#minor loop is = 4*(steps+1)
neighbours = 8				#The radius of neighbouring spins that are included in the local
							#field calculation
loops = 4					#The number of minor field loops to be done

#File information
Hcmax = [0.98,0.99,1,1.01,1.02]
folder = r'C:\Users\kjs18\Documents\RPM\Resevior\Control_New\Repeat_same_lattice'	#The folder for the files to be saved in.

#latticeload = r"C:\Users\kjs18\Documents\RPM\Resevior\InitialRPMLattice_Hmax8p420906e-02_steps20_Angle7p853982e-01_neighbours10_Loops4.npz"
#Define the system
#The parameters defined above go into the function below that defines the 
#characteristics of the lattice.
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice.square(Hc, Hc_std/100)	#Specify whether it is a square or kagome lattice
lattice.squareGroundState()
lattice.flipSpin(10,11)
lattice.flipSpin(12,11)
lattice.flipSpin(11,10)
lattice.flipSpin(11,12)
lattice.coerciveVertex(Hc)
plt.show()
