import rpmClass_Stable as rpm
import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
reload(rpm)

Lattice = rpm.ASI_RPM(1,1)

folder = r'D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD5.000000e-02_Happ1.060000e-01_count12'
folder = r'D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD5.000000e-02_Happ1.060000e-01_count7'
folder = r'D:\RPM_Rapid\SquareQDvHapp2\SquarePD_QD5.000000e-02_Happ1.050000e-01_count3'
Lattice.graphPeriod(folder, Hmax = '1p484924e-01T_')


