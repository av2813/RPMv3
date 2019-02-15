import rpmClass_Stable as rpm
import numpy as np
import matplotlib.pyplot as plt
from importlib import *
import os
import seaborn as sns

reload(rpm)


folder = r'D:\RPM_Rapid\TetrisPeriodDouble\PeriodDoublingData_QD1.000000e-07_Width4.000000e-08_Count1'

initial_file = r'InitialRPMLattice_Hmax1p414214e-01_steps10_Angle7p853982e-01_neighbours5_Loops10.npz'

Lattice = rpm.ASI_RPM(1,1)

Lattice.load(os.path.join(folder, initial_file))

field_angle=45.
Hmax = 0.1/np.cos(np.pi/4)

#savefolder = r'C:\Users\av2813\Desktop\RPM_tests'
#differentName = "PeriodDoublingData_QD1.000000e-07_Width4.000000e-08_Count1_30_Random3_finer20steps" 
#folderloc = os.path.join(savefolder, differentName) 
#Lattice.fieldSweep(Hmax, 20, field_angle, n=5, loops=30, folder = folderloc, q1 = True) 





grid2 = periodicBC(grid)
data = grid2
new_array = [tuple(row) for row in data]
uniques = np.unique(new_array)
print(uniques)
#grid2 = np.roll(grid, 13, axis = 0)
#print(grid2)

Lattice2 = rpm.ASI_RPM(lattice = grid2)

Lattice2.graph()
#Lattice.graph()
#Lattice2.graphCharge()
