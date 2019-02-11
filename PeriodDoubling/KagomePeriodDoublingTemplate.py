import rpmClass_Stable as rpm
import numpy as np
import os
import matplotlib.pyplot as plt
import re
from importlib import *         #Package to update the version of rpmClass_Stable

reload(rpm)





folder = os.getcwd()
lattice = rpm.ASI_RPM(1,1)
lattice.load(os.path.join(folder,'KagomePeriodDoublingLattice20x20.npz'))

field_angle=45.
Hmax = 0.1/np.cos(np.pi/4)