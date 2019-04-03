'''
Tests the effects of finite number of neighbour interactions
and finite number of field steps upon the hysteresis loop
with 3 different quenched disorder (1,5,10%)
'''

import rpmClass_Stable as rpm
import numpy as np
import os
import matplotlib.pyplot as plt
import re
from importlib import *         #Package to update the version of rpmClass_Stable

reload(rpm)



Hc = 0.1					#Coercive Field



bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 15e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters
size = 30					#Define the size of the lattice
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)

field_angle = 45.
folder = os.getcwd()





