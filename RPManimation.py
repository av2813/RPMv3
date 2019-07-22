#RPM animmation

import rpmClass_Stable as rpm
import numpy as np
from importlib import *
reload(rpm)
folder = r'D:\RPM_Rapid\ShaktiSSF_QDvsHapp2\ShaktiPD_QD1.000000e-01_Happ8.000000e-02_count12'
file = r'Counter0_LatticeState_Happlied1p131371e-01T_Htheta7p853982e-01Rad_neighbours5.npz'
Lattice =rpm.ASI_RPM(1,1)
Lattice.SSFAnimation(folder, file = file)
