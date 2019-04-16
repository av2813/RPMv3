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
reload(rpm)




Mx=[]	
My=[]

#Path to MFM image and lattice image
imageim = r"C:\Users\kjs18\Documents\RPM\RPM Code\T.PNG"#Path to MFM image
latticeim = r"C:\Users\kjs18\Documents\RPM\RPM Code\T.PNG"#Path to lattice image
folder = r"C:\Users\kjs18\Documents\RPM\RPM Code\Data\Defect_Simualtion\PinwheelHc"	#The folder for the files to be saved in.
npzfolder = r"C:\Users\kjs18\Documents\RPM\RPM Code\Data\defectnpz"
'''
for file in os.listdir(npzfolder):
	


#initiate image recognition files
#kagomedetect.kagome(latticeim, imageim)
#squaredetect.square(latticeim, imageim)

	npzfile = np.load(file)
	#loads magnetisation from files
	Mx = npzfile['arr_2']
	My = npzfile['arr_3']
	#print(Mx)
	#print(My)
	defect = file.replace(".npz","")
	#Material Parameters

	Hc = 0.062					#Coercive Field (T)
	Hc_std = [0, 1, 2, 3, 4, 5]					#Stanard deviation in the coercive field (as a percentage)
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

	#File information
	maxH = [0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.04]
	repeats = [1,2,3]

	for j in Hc_std:
	#Define the system
	#The parameters defined above go into the function below that defines the 
	#characteristics of the lattice.
			#Specify whether it is a square or kagome lattice
	#lattice.kagome(Hc, Hc_std/100)	#example of kagome
	#lattice.load(os.path.join(folder,'Lattice_counter5_Loop0_FieldApplied8p768124e-02_Angle7p853982e-01.npz'))
	#lattice.randomMag()

		

		for theta in field_angle:

			for H in maxH:
				for repeat in repeats:
					lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
						vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
	        			bar_width = bar_width, magnetisation = magnetisation)
					lattice.square(Hc, j/100)
					lattice.mfmLoad(Mx, My) #Loads MFM magnetisations
					newfolder = folder+'\\'+str(defect)+'\\Hc_std'+str(j)+'\\field_angle'+str(theta)+'\\maxH'+str(H)+'\\attempt'+str(repeat)
					lattice.fieldSweep((field_max*H), steps, theta, n=5, loops=5, folder = newfolder, q1 = False)
					
'''
#Material Parameters

Hc = 0.062					#Coercive Field (T)
Hc_std = [0, 1, 2, 3, 4, 5]					#Stanard deviation in the coercive field (as a percentage)
bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 14e-9		#Bar thickness in m
bar_width = 120e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 80e3)
size=6

lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice.square(Hc, Hc/100)	#Specify whether it is a square or kagome lattice
#lattice.mfmLoad(Mx,My)
#lattice.graphCharge()
#plt.show()



#loops through folders from a defect loop and creates a video with microstate animation. (Need to add lattice counter onto the video)
r=[]
def animation(folder, Hc):
	
	for QD in os.listdir(folder):
		if QD.endswith("Store"):
			r=2
		else:
			newpath = folder + '\\' + QD
			os.chdir(newpath)

			for angle in os.listdir(newpath):
				newpath2 = newpath + '\\' + angle
				print('OK')
				
				for maxfield in os.listdir(newpath2):
					if maxfield.endswith('txt'):
						r=1
					else:
						newpath3 = newpath2 + '\\' + maxfield
					
						for maxfield in os.listdir(newpath3):
							newpath5 = newpath3 +'\\' + maxfield
							os.chdir(newpath5)
							
							#for attempt in os.listdir(newpath4):
							#	newpath5 = newpath4 +'\\' + attempt
							#	os.chdir(newpath5)
							if 1==1:



								

								os.chdir(newpath5)
								print(newpath5)
								os.listdir(newpath5)
								os.makedirs("pngs2")
						
								a = [s for s in os.listdir(newpath5)
									if os.path.isfile(os.path.join(newpath5, s))]
								a.sort(key=lambda s: os.path.getmtime(os.path.join(newpath5, s)))					
								for file in a:

									if file.endswith(".npz") and file.startswith("Lattice"):
										
										
										lattice.load(os.path.join(newpath5,file))
										lattice.coerciveVertex(Hc)
										file = file.replace(".npz",".png")
										os.chdir(newpath5+'\\pngs2')
										plt.savefig(file)
										plt.close()
							
									else:
										r=1

								imagefolder=newpath5+'\\pngs2'
								os.chdir(imagefolder)
								video_name = 'Animation.avi'
								a = [s for s in os.listdir(imagefolder)
									if os.path.isfile(os.path.join(imagefolder, s))]
								a.sort(key=lambda s: os.path.getmtime(os.path.join(imagefolder, s)))
								print(a)
								#for f in os.listdir(imagefolder):
									#if f.endswith(".png"):
									#	images.append(f)
								frame = cv2.imread(os.path.join(imagefolder, a[0]))
								height, width, layers = frame.shape
								video = cv2.VideoWriter(video_name, 0, 3, (width,height))
								for image in a:

									video.write(cv2.imread(os.path.join(imagefolder, image)))
							
								else:
									r=1
								cv2.destroyAllWindows()
								video.release()


						
animation(folder, Hc)
'''

if 1==1:
	newpath5 = folder
	os.chdir(newpath5)
	if os.path.isdir(newpath5+'\\pngs'):
		os.rmdir("pngs")
	else:						
			r=1

	if os.path.isdir(newpath5+'\\pngs')	:
		r=1
	else:
		os.makedirs("pngs")
						
	a = [s for s in os.listdir(newpath5)
		if os.path.isfile(os.path.join(newpath5, s))]
	a.sort(key=lambda s: os.path.getmtime(os.path.join(newpath5, s)))					
	for file in a:

		if file.endswith(".npz") and file.startswith("Lattice"):
								
								
			lattice.load(os.path.join(newpath5,file))
			lattice.graphChargesave(file)
			file = file.replace(".npz",".png")
			os.chdir(newpath5+'\\pngs')
			plt.savefig(file)
					
		else:
			r=1

	imagefolder=newpath5+'\\pngs'
	os.chdir(imagefolder)
	video_name = 'Animation.avi'
	a = [s for s in os.listdir(imagefolder)
		if os.path.isfile(os.path.join(imagefolder, s))]
	a.sort(key=lambda s: os.path.getmtime(os.path.join(imagefolder, s)))
	print(a)
						#for f in os.listdir(imagefolder):
							#if f.endswith(".png"):
							#	images.append(f)
	frame = cv2.imread(os.path.join(imagefolder, a[0]))
	height, width, layers = frame.shape
	video = cv2.VideoWriter(video_name, 0, 3, (width,height))
	for image in a:

		video.write(cv2.imread(os.path.join(imagefolder, image)))
					
	else:
		r=1
	cv2.destroyAllWindows()
	video.release()
	'''
