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
from pylab import *
import matplotlib.colors as cl

import glob

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


#Path to MFM image and lattice image
imageim = r"C:\Users\Dell XPS 9530\Documents\Imonopole.PNG"#Path to MFM image
latticeim = r"C:\Users\Dell XPS 9530\Documents\Imonopole.PNG"#Path to lattice image
folder = r"C:\Users\Dell XPS 9530\Documents\PhD\RPM Code\Data"	#The folder for the files to be saved in.


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


#loops through folders from a defect loop and creates a video with microstate animation. (Need to add lattice counter onto the video)
r=[]
def animation(folder):
	
	for defect in os.listdir(folder):
		if defect.endswith("Store"):
			r=2
		else:
			newpath = folder + '\\' + defect
			os.chdir(newpath)

			for QD in os.listdir(newpath):
				newpath2 = newpath + '\\' + QD
				print('OK')
				
				for angle in os.listdir(newpath2):
					newpath3 = newpath2 + '\\' + angle
				
					for maxH in os.listdir(newpath3):
						newpath4 = newpath3 +'\\' + maxH
						os.chdir(newpath4)
						print(newpath4)
						
						if os.path.isdir(newpath4+'\\pngs'):
							r=1
						else:						
							os.makedirs("pngs")
					
			
						for file in os.listdir(newpath4):

							if file.endswith(".npz") and file.startswith("Lattice"):

								lattice.load(os.path.join(newpath4,file))
								lattice.graphChargesave(file)
								file = file.replace(".npz",".png")
								os.chdir(newpath4+'\\pngs')
								plt.savefig(file)
						
							else:
								r=1

						imagefolder=newpath4+'\\pngs'
						os.chdir(imagefolder)
						video_name = 'Animation.avi'
						images = []
						for f in os.listdir(imagefolder):
							if f.endswith(".png"):
								images.append(f)
						frame = cv2.imread(os.path.join(imagefolder, images[0]))
						height, width, layers = frame.shape
						video = cv2.VideoWriter(video_name, 0, 3, (width,height))
						for image in images:
							video.write(cv2.imread(os.path.join(imagefolder, image)))
				
						else:
							r=1
						cv2.destroyAllWindows()
						video.release()




					
						


listfolders(folder)

'''