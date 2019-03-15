import squaredetect
import kagomedetect
import os
import rpmClass_Stable as rpm
from importlib import *

import numpy as np	
import os
import matplotlib.pyplot as plt
from skimage import data, feature, exposure
from PIL import Image
import numpy as np
import argparse
import cv2
import math
from shapely import geometry
from matplotlib import pyplot as plt
from scipy import spatial
import itertools
import matplotlib.cm as cm
import matplotlib.colors as cl
reload(rpm)


Mx=[]	
My=[]

#Path to MFM image and lattice image
imageim = r"C:\Users\Dell XPS 9530\Documents\PhD\Samples\KS002\As grown\Poster\dpole1.png"#Path to MFM image
latticeim = r"C:\Users\Dell XPS 9530\Documents\PhD\Samples\KS002\As grown\Poster\dpole1.png"#Path to lattice image
folder = r"C:\Users\Dell XPS 9530\Documents\PhD\RPM Code\Data\Vmonopole\Hc_std5\field_angle135\maxH1"	#The folder for the files to be saved in.


#initiate image recognition files
#kagomedetect.kagome(latticeim, imageim)
squaredetect.square(latticeim, imageim)
npzfile = np.load('Outfile.npz')
#loads magnetisation from files
Mx = npzfile['arr_2']
My = npzfile['arr_3']
print(Mx)
print(My)

#Material Parameters

Hc = 0.062					#Coercive Field (T)
Hc_std = [1, 2, 3, 4, 5]					#Stanard deviation in the coercive field (as a percentage)
bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 14e-9		#Bar thickness in m
bar_width = 120e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 80e3)

#Lattice Parameters
size = 6					#Define the size of the lattice

#Minor loop Parameters
field_angle = [45, 135]
		#Angle at which the field will be applied in degrees
field_max = Hc/np.cos(45/180*np.pi)
field_min = 0.95*Hc/np.cos(45/180*np.pi)				#Maximum field to by applied at field angle measured in Telsa 
steps = 5	
Hsteps = 5				#Number of steps between the minimum value of the coercive field
							#and the maxium field specified above. Total number of steps in a 
							#minor loop is = 4*(steps+1)
neighbours = 4				#The radius of neighbouring spins that are included in the local
							#field calculation
loops = 6					#The number of minor field loops to be done
'''
#File information
maxH = [0.95, 0.96, 0.97, 0.98, 0.99, 1]

for j in Hc_std:
#Define the system
#The parameters defined above go into the function below that defines the 
#characteristics of the lattice.
	lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
	lattice.square(Hc, j/100)	#Specify whether it is a square or kagome lattice
#lattice.kagome(Hc, Hc_std/100)	#example of kagome
#lattice.load(os.path.join(folder,'Lattice_counter5_Loop0_FieldApplied8p768124e-02_Angle7p853982e-01.npz'))
#lattice.randomMag()

	lattice.mfmLoad(Mx, My) #Loads MFM magnetisations

	for theta in field_angle:

		for H in maxH:
			lattice.mfmLoad(Mx, My) #Loads MFM magnetisations
			newfolder = folder+'\\Hc_std'+str(j)+'\\field_angle'+str(theta)+'\\maxH'+str(H)
			lattice.fieldSweep((field_max*H), steps, theta, n=5, loops=5, folder = newfolder, q1 = False)
			
'''

lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice.square(Hc, Hc/100)	#Specify whether it is a square or kagome lattice
lattice.mfmLoad(Mx,My)
lattice.graphCharge()
plt.show()
#lattice.fieldSweepAnimation(folder)