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
from functools import partial
reload(rpm)
reload(squaredetect)
Mx=[]
My=[]
IslandProperties = []
C = []
Cnew = []
def distance_squared(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2

imageim = r"\\icnas2.cc.ic.ac.uk\kjs18\GitHub\RPMv3\Latticeimages\10 x10-GS.png" #Path to MFM image
latticeim = r"\\icnas2.cc.ic.ac.uk\kjs18\GitHub\RPMv3\Latticeimages\10 x10-GS.png" #Path to lattice image
folder = r'C:\Users\kjs18\Documents\RPM\RPM Code\Data\Defect_Simualtion\Tmonopole\Hc_std5\field_angle45\maxH0.97\attempt2'	#The folder for the files to be saved in.
size = 10
#squaredetect.square(imageim, latticeim, size)
file = r"\\icnas2.cc.ic.ac.uk\kjs18\GitHub\RPMv3\defectnpz\10x10GS.npz"

squaredetect.draw(10,1)
#Mx=[]	
#My=[]
os.chdir(r'\\icnas2.cc.ic.ac.uk\kjs18\GitHub\RPMv3')
npzfile = np.load("Outfile.npz")
Mx = npzfile['arr_2']
My = npzfile['arr_3']

#Material Parameters

Hc = 0.062					#Coercive Field (T)
Hc_std = 5					#Stanard deviation in the coercive field (as a percentage)
bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 20.5e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 80e3)

field_angle = 45.			#Angle at which the field will be applied in degrees
field_max = 0.95*Hc/np.cos(field_angle/180*np.pi)			#Maximum field to by applied at field angle measured in Telsa 
steps = 5					#Number of steps between the minimum value of the coercive field

magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 80e3)

#Lattice Parameters
				#Define the size of the lattice

Hsteps = 5				#Number of steps between the minimum value of the coercive field
							#and the maxium field specified above. Total number of steps in a 
							#minor loop is = 4*(steps+1)
neighbours = 4				#The radius of neighbouring spins that are included in the local
							#field calculation
loops = 6					#The number of minor field loops to be done


lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice.square(Hc, Hc_std/100)	#Specify whether it is a square or kagome lattice
'''
lattice.load(file)
lattice.coerciveVertex(Hc)
plt.show()
'''
lattice.mfmLoad(Mx,My)
lattice.vertexTypeMap()
plt.show()
'''
flipme = [(1,2), (2,5), (3,4), (4,1), (4,3), (5,4)]

for spins in flipme:
	lattice.flipSpin(spins[0]+6,spins[1]+6)


for x in range(18):
	for y in range(18):
		lattice.flipSpin(x,y)

lattice.vertexTypeMa2()
plt.show()

'''