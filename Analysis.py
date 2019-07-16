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
#reload(squaredetect)

Mx=[]
My=[]

#Path to MFM image and lattice image
imageim = r"C:\Users\kjs18\Documents\RPM\RPM Code\T.PNG" #Path to MFM image
latticeim = r"C:\Users\kjs18\Documents\RPM\RPM Code\T.PNG" #Path to lattice image
folderz = r'C:\Users\kjs18\Documents\RPM\RPM Code\Data\Defect_Simualtion\PinwheelHc'	#The folder for the files to be saved in.
file = r"C:\Users\kjs18\Documents\RPM\RPM Code\Data\Defect_Simualtion\vmonopole\Hc_std1\field_angle225\maxH1.01\attempt3\Lattice_counter0023_Loop0_FieldApplied-5p442683e-02_Angle3p926991e+00.npz"
Mx=[]	
My=[]


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
size = 6					#Define the size of the lattice

Hsteps = 5				#Number of steps between the minimum value of the coercive field
							#and the maxium field specified above. Total number of steps in a 
							#minor loop is = 4*(steps+1)
neighbours = 4				#The radius of neighbouring spins that are included in the local
							#field calculation
loops = 6					#The number of minor field loops to be done


lattice1 = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice1.square(Hc, Hc_std/100)	#Specify whether it is a square or kagome lattice

lattice2 = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)
lattice2.square(Hc, Hc_std/100)	#Specify whether it is a square or kagome lattice

r=[]
parameters_list = []
Hmax_list,Htheta_list, steps_list, n_list, loops_list = [],[],[],[],[]
Hc_list = []
Hc_std_list = []
field_steps_list = []
q_list = []
mag_list = []
monopole_list = []
vertex_list = []
GSloop = []
finalstateGS = []
changewithnoGS = []
nochange = []
cor_check = []
percentage=[]
relax = []
loop0 = []
loop1 = []
loop2 = []
loop3 = []
loop4 = []
loop10 = []
mostlyT1 = []
for QD in os.listdir(folderz):
	folder1 = os.path.join(folderz,QD)
	for angle in os.listdir(folder1):
		folders = os.path.join(folder1,angle)

		relax = []
		loop0 = []
		loop1 = []
		loop2 = []
		loop3 = []
		loop4 = []
		loop10 = []
		nochange = []
		mostlyT1=[]
		interesting =[]

		for MaxH in os.listdir(folders):
			print(MaxH)
			folder2 = os.path.join(folders,MaxH)
			for attempt in os.listdir(folder2):
				folder = os.path.join(folder2, attempt)
				#newpath2 = os.path.join(newpath, attempt)
				print(folder)
			#Checks for a change after H+

				#loops through ends of loops and sees if they're in the ground state
				for files in os.listdir(folder):
					if 'Lattice_counter0023' in files:
						lattice1.load(os.path.join(folder,files))
						if lattice1.groundStateCheck() is True:
							GSloop = 0
						else:
							for files in os.listdir(folder):
								if 'Lattice_counter0047' in files:
									lattice1.load(os.path.join(folder,files))
									if lattice1.groundStateCheck() is True:
										GSloop = 1
									else:
										for files in os.listdir(folder):
											if 'Lattice_counter0071' in files:
												lattice1.load(os.path.join(folder,files))
												if lattice1.groundStateCheck() is True:
													GSloop = 2
												else:
													for files in os.listdir(folder):
														if 'Lattice_counter0095' in files:
															lattice1.load(os.path.join(folder,files))
															if lattice1.groundStateCheck() is True:
																GSloop = 3
															else:
																for files in os.listdir(folder):
																	if 'Lattice_counter00119' in files:
																		lattice1.load(os.path.join(folder,files))
																		if lattice1.groundStateCheck() is True:
																			GSloop = 4
																		else:
																			GSloop = 10
																			percentages = lattice1.vertexTypePercentage()
																			T1 = percentages[0]
				print(folder)
				print("GS loop = " + str(GSloop))

				#Checks to see if there are any changes
				for file in os.listdir(folder):
					if 'RPMStateInfo' in file:
						npzfile = np.load(os.path.join(folder,file))
						items = (npzfile['arr_2'])
						if lattice1.all_same(items) == True:
							nochanges = 1
						else:
							nochanges = 0

				#appends no change list
				if percentage == 1:
					mostlyT1.append([folder, T1])

				if nochanges == 1:
					nochange.append(folder)

				if GSloop == 0:
					loop0.append(folder)

				if GSloop == 1:
					loop1.append(folder)

				if GSloop == 2:
					loop2.append(folder)

				if GSloop == 3:
					loop3.append(folder)

				if GSloop == 4:
					loop4.append(folder)

				if GSloop == 10:
					loop10.append([folder, T1])

				if GSloop > 3 and T1 !=0:
					interesting.append([folder,T1])
		

		os.chdir(folders)
		with open('info.txt', 'w') as f:

			f.write("\n No changes \n")
			for item in nochange:
				f.write("%s\n" % item)

			f.write("\n Loop1 relaxation\n")
			for item in loop0:
				f.write("%s\n" % item)

			f.write("\n Loop2 relaxation\n")
			for item in loop1:
				f.write("%s\n" % item)

			f.write("\n Loop3 relaxation\n")
			for item in loop2:
				f.write("%s\n" % item)

			f.write("\n Loop4 relaxation\n")
			for item in loop3:
				f.write("%s\n" % item)

			f.write("\n Loop5 relaxation\n")
			for item in loop4:
				f.write("%s\n" % item)
		    
			f.write("\n Changes and no relaxation after 1 loop \n")
			for item in loop10:
				f.write("%s\n" % item)   

			f.write("\n Interesting")
			for item in interesting:
				f.write("%s\n" % item)
		del mostlyT1
		del nochange
		del loop0
		del loop1
		del loop2
		del loop3
		del loop4
		del loop10
		del interesting
    
		'''

                    self.correlation(Initialstate, lattice4)
                        
                    if 'Lattice_counter0047' in file: #checks to see if the lattice is in the ground state after 1 loop.
                        print(file)
                        self.load(os.path.join(newpath2,file))
                        if self.groundStateCheck() is True:
                            loop1GS.append(newpath2)
                        else:    
                            for file in os.listdir(newpath2):
                                if 'RPMStateInfo' in file:
                                    npzfile = np.load(os.path.join(newpath2,file))
                                    parameters_list.append(npzfile['arr_0'])
                                    print(parameters_list)
                                    Hmax_list.append(npzfile['arr_0'][0])
                                    steps_list.append(npzfile['arr_0'][1])
                                    Htheta_list.append(npzfile['arr_0'][2])
                                    n_list.append(npzfile['arr_0'][3])
                                    loops_list.append(npzfile['arr_0'][4])
                                    Hc_list.append(npzfile['arr_0'][5])
                                    Hc_std_list.append(npzfile['arr_0'][6])
                                    field_steps_list.append(npzfile['arr_1'])
                                    q_list.append(npzfile['arr_2'])
                                    mag_list.append(npzfile['arr_3'])
                                    monopole_list.append(npzfile['arr_4'])
                                    vertex_list.append(npzfile['arr_5'])

                                
                for file in os.listdir(newpath2):
                    if 'FinalRPM' in file: #checks to see if the lattice finishes in the ground state
                        self.load(os.path.join(newpath2,file))
                        if self.groundStateCheck() is True:
                            finalstateGS.append(newpath2)
                        else:
                            for file in os.listdir(newpath2):
                                if 'RPMStateInfo' in file:
                                    npzfile = np.load(os.path.join(newpath2,file))
                                    if self.all_same(npzfile['arr_2']) is True:
                                        nochange.append(newpath2)
                                    else:
                                        changewithnoGS.append(newpath)
                                        for attempt in os.listdir(newpath):
                                            if '1' in attempt:
                                                r=1
                                            else:
                                                newpath2 = os.path.join(newpath, attempt)
                                                for file in os.listdir(newpath2):
                                                    if 'Lattice_counter0047' in file: #checks to see if the lattice is in the ground state after 1 loop.
                                                        print(file)
                                                        self.load(os.path.join(newpath2,file))
                                                        if self.groundStateCheck() is True:
                                                            loop1GS.append(newpath2)
                                                        else:    
                                                            for file in os.listdir(newpath2):
                                                                if 'RPMStateInfo' in file:
                                                                    npzfile = np.load(os.path.join(newpath2,file))
                                                                    parameters_list.append(npzfile['arr_0'])
                                                                    print(parameters_list)
                                                                    Hmax_list.append(npzfile['arr_0'][0])
                                                                    steps_list.append(npzfile['arr_0'][1])
                                                                    Htheta_list.append(npzfile['arr_0'][2])
                                                                    n_list.append(npzfile['arr_0'][3])
                                                                    loops_list.append(npzfile['arr_0'][4])
                                                                    Hc_list.append(npzfile['arr_0'][5])
                                                                    Hc_std_list.append(npzfile['arr_0'][6])
                                                                    field_steps_list.append(npzfile['arr_1'])
                                                                    q_list.append(npzfile['arr_2'])
                                                                    mag_list.append(npzfile['arr_3'])
                                                                    monopole_list.append(npzfile['arr_4'])
                                                                    vertex_list.append(npzfile['arr_5'])

                
for Hmax, loops, steps, q, mag, monopole, vertex, Hc, angle in zip(Hmax_list, \
                loops_list, steps_list, q_list, mag_list, monopole_list, vertex_list, Hc_list, Htheta_list):
    self.plotCorrelation(folder, q, Hmax, loops, steps, Hc, angle)

    #self.plotMagnetisation(folder, q, Hmax, loops, steps, Hc)
    #self.plotMonopole(folder, monopole, Hmax, loops, steps)
    #self.plotVertex(folder, vertex, Hmax, loops, steps)
os.chdir(folder)
with open('info.txt', 'w') as f:
    f.write("Ground state after 1 loop \n")
    for item in loop1GS:
        f.write("%s\n" % item)   
    f.write("\n Ground State at end \n")
    for item in finalstateGS:
        f.write("%s\n" % item)
    for item in loop1GS:
        if item in finalstateGS:
            r=1
        else:
            f.write("%s\n" % item)
    f.write("\n No changes \n")
    for item in nochange:
        f.write("%s\n" % item)

    f.write("\n Loops that change but dont settle into the ground state \n")
    for item in changewithnoGS:
        f.write("%s\n" % item)
        r=[]
parameters_list = 0
Hmax_list,Htheta_list, steps_list, n_list, loops_list = 0,0,0,0,0
Hc_list = 0
Hc_std_list = 0
field_steps_list = 0
q_list = 0
mag_list = 0
monopole_list = 0
vertex_list = 0
loop1GS = 0
finalstateGS = 0
changewithnoGS = 0
nochange = 0
cor_check = 0

'''