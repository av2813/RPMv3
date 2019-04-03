import rpmClass_Stable as rpm
import numpy as np
import os
import matplotlib.pyplot as plt
import re
from importlib import *         #Package to update the version of rpmClass_Stable

reload(rpm)


Hc = 0.1
Hc_std = 0.1


folder = os.getcwd()
lattice = rpm.ASI_RPM(5,5)
lattice.tetris(Hc, Hc_std)
steps = 20

field_angle=-45.
Hmax = 0.1

lattice.relax(np.array([-1., 1., 0.]), n=1)




