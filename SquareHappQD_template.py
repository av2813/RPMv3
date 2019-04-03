
import rpmClass_Stable as rpm
import numpy as np
import os
import matplotlib.pyplot as plt
import re
from importlib import *         #Package to update the version of rpmClass_Stable

reload(rpm)

steps = 20
folder = os.getcwd()

Hc = 0.1					#Coercive Field

Hmax = 0.1
field_angle = 45

bar_length = 400e-9			#Bar length in m
vertex_gap = 100e-9			#Vertex gap in m
bar_thickness = 15e-9		#Bar thickness in m
bar_width = 200e-9			#Bar width in m
magnetisation = 800e3		#Saturation magnetisation of material in A/m (permalloy is 830e3)

#Lattice Parameters
QD = 0.05

size = 20

