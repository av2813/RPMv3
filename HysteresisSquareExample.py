import rpmClass_Stable as rpm
import numpy as np
import os
import matplotlib.pyplot as plt
import re
from importlib import *         #Package to update the version of rpmClass_Stable

reload(rpm)



Hc = 0.1					#Coercive Field
Hc_std1 = 0.1


bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 15e-9		#Bar thickness in m
bar_width = 80e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters
size = 50					#Define the size of the lattice
lattice = rpm.ASI_RPM(size,size,bar_length = bar_length, \
					vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        			bar_width = bar_width, magnetisation = magnetisation)

folder = os.getcwd()
folderloc = os.path.join(os.getcwd(), 'Square_Hysteresis' % locals())
if not os.path.exists(folderloc):
    os.makedirs(folderloc)

lattice.square(Hc, Hc_std1)
lattice.save('SquareHysteresisLattice50x50_%(Hc_std1)e' %locals())

field_angle=45.

differentName = 'HysteresisData_QD%(Hc_std1)e' %locals()
folderloc = os.path.join(folder, differentName)
lattice.Hysteresis(50, field_angle, folder = folderloc)


