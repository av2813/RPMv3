import rpmClass_Stable as rpm
import numpy as np
import os
import matplotlib.pyplot as plt
import re
from importlib import *         #Package to update the version of rpmClass_Stable

reload(rpm)





folder = os.getcwd()
lattice = rpm.ASI_RPM(1,1)


field_angle=45.
Hmax = 0.1/np.cos(np.pi/4)






lattice.load(os.path.join(folder,"2BrickworkPeriodDoublingLattice20x20.npz")) 
lattice.changeQuenchedDisorder(0.024000) 
lattice.changeWidth(2.000000e-08) 
differentName = "PeriodDoublingData_QD2.400008e-02_Width2.000000e-08_Count2" 
folderloc = os.path.join(folder, differentName) 
lattice.fieldSweep(Hmax, 10, field_angle, n=5, loops=10, folder = folderloc, q1 = True) 
