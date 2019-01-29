import rpmClass_Stable as rpm
from importlib import *
import numpy as np
reload(rpm)		#make sure that the class is updated with any changes

#parameters
Hc = 0.062
Hc_std = 0.05
bar_length = 63e-9
vertex_gap = 125e-9
bar_thickness = 5e-9
bar_width = 23e-9
magnetisation = 800e3

number = 100
number = 100
Lattice = rpm.ASI_RPM(number,number,bar_length = bar_length, vertex_gap = vertex_gap, bar_thickness = bar_thickness, \
        bar_width = bar_width, magnetisation = magnetisation)

Lattice.kagome()
print(((Lattice.magMoment(np.pi/3))*2.5e-3*2.5e-3))



