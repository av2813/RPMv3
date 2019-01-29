import numpy as np
import os
import matplotlib.pyplot as plt
import rpmClass_Stable as rpm
import re
from importlib import *         #Package to update the version of rpmClass_Stable
import seaborn as sns

reload(rpm)
sns.set_style("ticks")
sns.set_palette("colorblind")


				#Define the size of the lattice



folder = os.getcwd()
lattice = rpm.ASI_RPM(1,1)
lattice.load(os.path.join(folder,'SquarePeriodDoublingLattice20x20.npz'))

field_angle=45.
Hmax = 0.1/np.cos(np.pi/4)

lattice.randomMag()




lattice.changeQuenchedDisorder(0.060000) 
lattice.changeWidth(3.500000e-07) 
differentName = "PeriodDoublingData_QD6.000000e-02_Width3.500000e-07_1" 
folderloc = os.path.join(folder, differentName) 
lattice.fieldSweep(Hmax, 10, field_angle, n=5, loops=10, folder = folderloc, q1 = True) 
